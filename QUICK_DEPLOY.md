# 🚀 QUICK DEPLOYMENT GUIDE - Railway

Your bot is now on GitHub! Follow these steps to deploy for FREE:

## Step 1: Railway Setup
1. **Go to Railway** (should be open in your browser)
2. **Sign up** with your GitHub account
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**: `MaakaaliCreations/maa-kaali-bot`

## Step 2: Add Environment Variables
In Railway dashboard, go to your project → "Variables" tab and add:

```
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
ADMIN_CHAT_ID=YOUR_ADMIN_CHAT_ID_HERE
SHOPIFY_STORE_DOMAIN=maakaalicreations
SHOPIFY_API_ACCESS_TOKEN=YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE
```

## Step 3: Deploy
Railway will automatically:
- ✅ Detect it's a Python app
- ✅ Install dependencies from `requirements.txt`
- ✅ Start your bot using `telegram_bot.py`
- ✅ Keep it running 24/7

## Step 4: Test Your Bot
1. Open Telegram
2. Search for your bot
3. Send `/start`
4. Test all features!

## 🎉 DONE!
Your bot will run **FREE FOREVER** on Railway!

---
**Need help?** Check the full `DEPLOYMENT.md` for detailed instructions. 