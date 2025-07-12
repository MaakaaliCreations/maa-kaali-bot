# 🚀 Free Deployment Guide for Maa Kaali Bot

This guide will help you deploy your Telegram bot for **FREE FOREVER** using various platforms.

## 🎯 Quick Start - Choose Your Platform

### Option 1: Railway (Recommended - Easiest)
### Option 2: Render (Alternative)
### Option 3: Replit (For Development)

---

## 🚂 Option 1: Railway Deployment (Recommended)

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Name it: `maa-kaali-bot`
4. Make it **Public** (required for free deployment)
5. Click "Create repository"

### Step 2: Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/maa-kaali-bot.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `maa-kaali-bot` repository
5. Railway will automatically detect it's a Python app

### Step 4: Configure Environment Variables
In Railway dashboard, go to your project → "Variables" tab and add:

```
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
ADMIN_CHAT_ID=YOUR_ADMIN_CHAT_ID_HERE
SHOPIFY_STORE_DOMAIN=maakaalicreations
SHOPIFY_API_ACCESS_TOKEN=YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE
```

### Step 5: Deploy
Railway will automatically deploy your bot! 🎉

---

## 🌐 Option 2: Render Deployment

### Step 1: Create GitHub Repository (same as above)

### Step 2: Deploy on Render
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: `maa-kaali-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python telegram_bot.py`

### Step 3: Add Environment Variables
In Render dashboard, add the same environment variables as Railway.

---

## 🎨 Option 3: Replit Deployment

### Step 1: Create Repl
1. Go to [Replit.com](https://replit.com)
2. Click "Create Repl" → "Python"
3. Name it: `maa-kaali-bot`

### Step 2: Upload Files
Upload your `telegram_bot.py` and `requirements.txt` files

### Step 3: Add Secrets
In Replit, go to "Tools" → "Secrets" and add:
- `BOT_TOKEN`
- `ADMIN_CHAT_ID`
- `SHOPIFY_STORE_DOMAIN`
- `SHOPIFY_API_ACCESS_TOKEN`

### Step 4: Run
Click "Run" and your bot will start!

---

## 🔧 Environment Variables Setup

Your bot needs these environment variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `BOT_TOKEN` | `YOUR_BOT_TOKEN_HERE` | Your Telegram bot token |
| `ADMIN_CHAT_ID` | `YOUR_ADMIN_CHAT_ID_HERE` | Your admin chat ID |
| `SHOPIFY_STORE_DOMAIN` | `maakaalicreations` | Your Shopify store name |
| `SHOPIFY_API_ACCESS_TOKEN` | `YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE` | Your Shopify API token |

---

## 📱 Testing Your Bot

1. Open Telegram
2. Search for your bot: `@YOUR_BOT_USERNAME`
3. Send `/start`
4. Test all menu options

---

## 🔄 Auto-Restart Setup

### Railway (Automatic)
Railway automatically restarts your bot if it crashes.

### Render (Automatic)
Render automatically restarts your bot.

### Replit (Manual)
You need to manually restart if it crashes.

---

## 💰 Cost Breakdown

| Platform | Cost | Limitations |
|----------|------|-------------|
| **Railway** | **FREE** | 500 hours/month, 512MB RAM |
| **Render** | **FREE** | 750 hours/month, 512MB RAM |
| **Replit** | **FREE** | Always-on requires paid plan |

---

## 🛠 Troubleshooting

### Bot Not Responding
1. Check if environment variables are set correctly
2. Verify bot token is valid
3. Check deployment logs

### Shopify API Errors
1. Verify Shopify API token has correct permissions
2. Check if store domain is correct
3. Ensure products are published in Shopify

### Deployment Fails
1. Check if all files are committed to GitHub
2. Verify `requirements.txt` is present
3. Check deployment logs for errors

---

## 📞 Support

If you need help:
1. Check the logs in your deployment platform
2. Test the bot locally first
3. Verify all environment variables are set

---

## 🎉 Success!

Once deployed, your bot will run 24/7 for FREE! 

**Your customers can now:**
- Browse your saree collection
- View offers and discounts
- Place orders online
- Get customer support
- Track their orders

---

<<<<<<< HEAD
*Last updated: December 2024* 

## 🚀 **LET'S FIX THIS STEP BY STEP:**

### **Step 1: Update requirements.txt**
1. Go to: https://github.com/MaakaaliCreations/maa-kaali-bot/blob/main/requirements.txt
2. Click the **pencil icon** (Edit this file)
3. Change line 1 from `python-telegram-bot==20.7` to `python-telegram-bot==20.6`
4. Click **"Commit changes"** at the bottom

### **Step 2: Update telegram_bot.py**
1. Go to: https://github.com/MaakaaliCreations/maa-kaali-bot/blob/main/telegram_bot.py
2. Click the **pencil icon** (Edit this file)
3. Find these lines and make sure they show placeholders:
   ```python
   BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
   ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "YOUR_ADMIN_CHAT_ID_HERE")
   SHOPIFY_API_ACCESS_TOKEN = os.getenv("SHOPIFY_API_ACCESS_TOKEN", "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE")
   ```
4. Click **"Commit changes"**

### **Step 3: Check New Commit**
After making these changes, you should see a new commit in your repository.

### **Step 4: Go to Render**
1. Go to: https://render.com/dashboard
2. Click on your `maa-kaali-bot` service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**

**Start with Step 1 (updating requirements.txt) and let me know when you're done! 🚀** 
=======
*Last updated: December 2024* 
>>>>>>> 269b789d4fc37c25a85f6f71f1336e0e327253b4
