#!/usr/bin/env python3
"""
Test script for Maa Kaali Creations Telegram Bot
Run this to test your bot before deployment
"""

import os
import sys
from telegram_bot import main

def test_bot():
    """Test the bot configuration"""
    print("🤖 Testing Maa Kaali Creations Bot...")
    
    # Check if required files exist
    required_files = ['telegram_bot.py', 'requirements.txt', 'logo.png']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Missing required file: {file}")
            return False
        else:
            print(f"✅ Found: {file}")
    
    # Check environment variables
    env_vars = ['BOT_TOKEN', 'ADMIN_CHAT_ID', 'SHOPIFY_STORE_DOMAIN', 'SHOPIFY_API_ACCESS_TOKEN']
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ Environment variable set: {var}")
        else:
            print(f"⚠️  Environment variable not set: {var} (will use default)")
    
    print("\n🎯 Bot is ready for deployment!")
    print("📋 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Choose a deployment platform (Railway recommended)")
    print("3. Set environment variables in your deployment platform")
    print("4. Deploy!")
    
    return True

if __name__ == "__main__":
    test_bot() 