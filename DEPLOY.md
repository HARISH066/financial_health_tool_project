# Deployment Guide - Step by Step

## IMPORTANT: Deploy Backend FIRST, then Frontend!

---

## Part 1: Deploy Backend on Render (5 minutes)

### Step 1: Sign up for Render
1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with your GitHub account
4. Authorize Render to access your repositories

### Step 2: Create Web Service
1. Click "New +" button (top right)
2. Select "Web Service"
3. Click "Connect" next to your repository: `financial_health_tool_project`

### Step 3: Configure Backend
Fill in these settings:

- **Name**: `financial-health-backend` (or any name you like)
- **Region**: Oregon (US West) - or closest to you
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Instance Type**: Free

### Step 4: Deploy
1. Click "Create Web Service"
2. Wait 3-5 minutes for deployment
3. Once deployed, you'll see "Your service is live 🎉"
4. **COPY YOUR BACKEND URL** - it will look like:
   ```
   https://financial-health-backend-xxxx.onrender.com
   ```

### Step 5: Test Backend
Open your backend URL in browser, you should see:
```json
{"status": "Backend running successfully"}
```

✅ Backend is ready!

---

## Part 2: Deploy Frontend on Vercel (3 minutes)

### Step 1: Sign up for Vercel
1. Go to https://vercel.com
2. Click "Sign Up"
3. Choose "Continue with GitHub"
4. Authorize Vercel

### Step 2: Import Project
1. Click "Add New..." → "Project"
2. Find and select your repository: `financial_health_tool_project`
3. Click "Import"

### Step 3: Configure Frontend
Fill in these settings:

- **Framework Preset**: Create React App (should auto-detect)
- **Root Directory**: Click "Edit" → Select `frontend` folder
- **Build Command**: `npm run build` (default)
- **Output Directory**: `build` (default)
- **Install Command**: `npm install` (default)

### Step 4: Add Environment Variable
**CRITICAL STEP** - This connects frontend to backend:

1. Click "Environment Variables" section
2. Add variable:
   - **Name**: `REACT_APP_API_URL`
   - **Value**: Your Render backend URL (from Part 1, Step 4)
   - Example: `https://financial-health-backend-xxxx.onrender.com`
3. Click "Add"

### Step 5: Deploy
1. Click "Deploy"
2. Wait 2-3 minutes
3. Once done, you'll see "Congratulations! 🎉"
4. Click "Visit" or copy your frontend URL:
   ```
   https://financial-health-tool-xxxx.vercel.app
   ```

✅ Frontend is deployed!

---

## Part 3: Update CORS (IMPORTANT!)

Your frontend can't talk to backend without this step!

### Step 1: Update backend/app/main.py

Open `backend/app/main.py` and find the CORS section (around line 18).

Replace:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

With (add your Vercel URL):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://financial-health-tool-xxxx.vercel.app"  # YOUR VERCEL URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Step 2: Push Changes
```bash
git add backend/app/main.py
git commit -m "Update CORS for Vercel deployment"
git push
```

### Step 3: Wait for Auto-Deploy
- Render will automatically redeploy (takes 2-3 minutes)
- Watch the deployment in Render dashboard

✅ CORS is configured!

---

## Part 4: Test Everything! 🎉

### Step 1: Open Your Frontend
Go to your Vercel URL: `https://financial-health-tool-xxxx.vercel.app`

### Step 2: Upload CSV
1. Click "Choose File"
2. Select `sample_data.csv` or any financial CSV
3. Click "Analyze"

### Step 3: Verify Results
You should see:
- ✅ KPI cards with metrics
- ✅ Revenue vs Expense chart
- ✅ Profit pie chart
- ✅ Cash flow forecast
- ✅ Credit status
- ✅ Industry benchmark
- ✅ AI insights

### If Upload Fails:
1. Open browser console (F12)
2. Check for CORS errors
3. Verify backend URL in Vercel environment variables
4. Make sure CORS is updated in backend

---

## Part 5: Update README

Add your URLs to README.md:

```markdown
## 🚀 Live Links

- **GitHub**: https://github.com/HARISH066/financial_health_tool_project
- **Frontend**: https://financial-health-tool-xxxx.vercel.app
- **Backend API**: https://financial-health-backend-xxxx.onrender.com
- **Demo Video**: [Add after recording]
```

Then push:
```bash
git add README.md
git commit -m "Add deployment URLs"
git push
```

---

## Quick Reference

### Your URLs:
- **GitHub**: https://github.com/HARISH066/financial_health_tool_project
- **Backend**: [Copy from Render]
- **Frontend**: [Copy from Vercel]

### Deployment Dashboards:
- **Render**: https://dashboard.render.com
- **Vercel**: https://vercel.com/dashboard

### Troubleshooting:
- **CORS Error**: Update backend CORS with Vercel URL
- **API Not Found**: Check REACT_APP_API_URL in Vercel
- **Build Failed**: Check logs in deployment dashboard

---

## Done! 🎉

Your app is now live and working. Test the CSV upload to make sure everything works!
