# Deployment Guide

## Git Setup & Push

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Financial Health Assessment Tool"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

## Backend Deployment (Render - Free)

1. Go to https://render.com and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: financial-health-backend
   - **Environment**: Python 3
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variable:
   - `DATABASE_URL`: (Render will provide PostgreSQL URL if you add database)
6. Click "Create Web Service"
7. Copy the deployed URL (e.g., https://your-app.onrender.com)

## Frontend Deployment (Vercel - Free)

1. Go to https://vercel.com and sign up
2. Click "Import Project"
3. Connect your GitHub repository
4. Configure:
   - **Framework**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
5. Add Environment Variable:
   - `REACT_APP_API_URL`: Your backend URL from Render
6. Click "Deploy"
7. Copy the deployed URL (e.g., https://your-app.vercel.app)

## Update CORS in Backend

After deploying frontend, update `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-app.vercel.app"  # Add your Vercel URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then commit and push again.

## Update README

Add your deployed URLs to README.md:
- Frontend URL
- Backend URL
- Demo Video URL (after recording)

## Record Demo Video

1. Use Loom (https://loom.com) or OBS Studio
2. Show:
   - Upload CSV file
   - Dashboard with all features
   - Explain key features
3. Upload to YouTube (Unlisted) or Google Drive
4. Add link to README.md

## Final Checklist

- [ ] Code pushed to GitHub (public repo)
- [ ] Backend deployed on Render
- [ ] Frontend deployed on Vercel
- [ ] CORS updated with frontend URL
- [ ] Demo video recorded and uploaded
- [ ] All URLs added to README.md
- [ ] Test all links work
