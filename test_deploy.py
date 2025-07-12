#!/usr/bin/env python3
"""
Simple test script to verify bot deployment
"""

import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all imports work"""
    try:
        from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
        from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_environment():
    """Test environment variables"""
    required_vars = ['BOT_TOKEN', 'ADMIN_CHAT_ID', 'SHOPIFY_STORE_DOMAIN', 'SHOPIFY_API_ACCESS_TOKEN']
    
    for var in required_vars:
        value = os.getenv(var)
        if value and value != f"YOUR_{var}_HERE":
            print(f"✅ {var}: Set")
        else:
            print(f"⚠️ {var}: Not set or using placeholder")
    
    return True

def test_bot_creation():
    """Test if bot can be created"""
    try:
        from telegram.ext import Application
        
        # Use a test token
        test_token = "1234567890:TEST_TOKEN_FOR_TESTING"
        app = Application.builder().token(test_token).build()
        print("✅ Bot application created successfully")
        return True
    except Exception as e:
        print(f"❌ Bot creation error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing bot deployment...")
    print()
    
    test_imports()
    print()
    test_environment()
    print()
    test_bot_creation()
    print()
    print("✅ All tests completed!") 