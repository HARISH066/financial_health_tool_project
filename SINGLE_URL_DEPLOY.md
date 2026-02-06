# Single URL Deployment Guide

Deploy your entire app (frontend + backend) on **ONE URL** using Render.

---

## 🚀 Deploy on Render (Single URL)

### Step 1: Sign Up
1. Go to **https://render.com**
2. Click "Get Started for Free"
3. Sign up with GitHub
4. Authorize Render

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Find and click **"Connect"** next to: `financial_health_tool_project`

### Step 3: Configure
Fill in these settings:

- **Name**: `financial-health-tool` (or any name)
- **Region**: Oregon (US West)
- **Branch**: `main`
- **Root Directory**: Leave empty
- **Runtime**: Python 3
- **Build Command**:
  ```
  cd frontend && npm install && npm run build && cd ../backend && pip install -r requirements.txt
  ```
- **Start Command**:
  ```
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```
- **Instance Type**: Free

### Step 3.5: Add PostgreSQL Database (Required)

**IMPORTANT**: The project requires PostgreSQL as per requirements.

1. Scroll down to **"Environment Variables"** section
2. Click **"Add from Database"** button
3. Click **"Create Database"**
4. Configure:
   - **Name**: `financial-health-db`
   - **Database**: Leave default (PostgreSQL)
   - **Region**: Same as your web service (Oregon)
   - **Instance Type**: Free
5. Click **"Create Database"**
6. Wait 1-2 minutes for database creation
7. Back in your web service, click **"Add from Database"** again
8. Select your database: `financial-health-db`
9. It will automatically add `DATABASE_URL` environment variable ✅

### Step 3.6: Environment Variables Summary

After adding PostgreSQL, you should see:
- ✅ `DATABASE_URL` - Auto-added from database (PostgreSQL connection string)

**Optional** (for real LLM, not required):
- `OLLAMA_URL` - If you have Ollama server
- `MODEL_NAME` - LLM model name

**The app works great with just PostgreSQL!**

### Step 4: Deploy
1. Click **"Create Web Service"**
2. Wait 5-7 minutes (it builds both frontend and backend)
3. Watch the logs - you'll see:
   - Installing npm packages
   - Building React app
   - Installing Python packages
   - Starting server

### Step 5: Get Your URL
Once deployed, you'll see:
```
Your service is live 🎉
https://financial-health-tool-xxxx.onrender.com
```

**This is your SINGLE URL!** ✅

---

## 🎮 Test Your App

1. Open your Render URL: `https://financial-health-tool-xxxx.onrender.com`
2. You should see the dashboard
3. Upload `sample_data.csv`
4. Click "Analyze"
5. See all the results!

---

## 📝 Update README

Add your URL to README.md:

```markdown
## 🚀 Live Links

- **Live App**: https://financial-health-tool-xxxx.onrender.com
- **GitHub**: https://github.com/HARISH066/financial_health_tool_project
- **Demo Video**: [Add after recording]
```

Then push:
```bash
git add README.md
git commit -m "Add live deployment URL"
git push
```

---

## ⚠️ Important Notes

### First Load Delay
- Render free tier spins down after 15 minutes of inactivity
- First load may take 30-60 seconds to wake up
- Subsequent loads are instant

### If Build Fails
Check the logs in Render dashboard. Common issues:
- Node.js version: Render uses Node 14 by default
- If needed, add `.node-version` file with `18` in it

---

## 🎉 Done!

You now have:
- ✅ Single URL for entire app
- ✅ Frontend and backend together
- ✅ Free hosting
- ✅ Auto-deploys on git push

**Your submission URL**: `https://financial-health-tool-xxxx.onrender.com`
