#!/usr/bin/env python3
"""
GitHub Deployment Helper Script
Automates the process of creating a GitHub repository and pushing your bot
"""

import os
import subprocess
import sys
import webbrowser
from pathlib import Path

def print_banner():
    """Print a beautiful banner"""
    print("=" * 60)
    print("🚀 MAA KAALI BOT - FREE DEPLOYMENT HELPER")
    print("=" * 60)
    print()

def check_git_status():
    """Check if git is initialized and has commits"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Git repository not initialized!")
            return False
        
        # Check if we have commits
        result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True)
        if not result.stdout.strip():
            print("❌ No commits found!")
            return False
            
        print("✅ Git repository is ready!")
        return True
    except FileNotFoundError:
        print("❌ Git is not installed! Please install Git first.")
        return False

def get_github_username():
    """Get GitHub username from user"""
    print("📝 Please enter your GitHub username:")
    username = input("Username: ").strip()
    return username

def create_github_repo_instructions(username):
    """Show instructions for creating GitHub repository"""
    print("\n" + "=" * 50)
    print("📋 STEP 1: Create GitHub Repository")
    print("=" * 50)
    print()
    print("1. Go to: https://github.com/new")
    print("2. Repository name: maa-kaali-bot")
    print("3. Make it PUBLIC (required for free deployment)")
    print("4. Don't initialize with README (we already have one)")
    print("5. Click 'Create repository'")
    print()
    
    # Open GitHub in browser
    print("🌐 Opening GitHub in your browser...")
    webbrowser.open("https://github.com/new")
    
    input("Press Enter when you've created the repository...")

def push_to_github(username):
    """Push code to GitHub"""
    print("\n" + "=" * 50)
    print("📤 STEP 2: Push to GitHub")
    print("=" * 50)
    print()
    
    # Add remote origin
    remote_url = f"https://github.com/{username}/maa-kaali-bot.git"
    
    try:
        # Remove existing remote if any
        subprocess.run(['git', 'remote', 'remove', 'origin'], capture_output=True)
        
        # Add new remote
        result = subprocess.run(['git', 'remote', 'add', 'origin', remote_url], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Failed to add remote: {result.stderr}")
            return False
            
        # Set branch to main
        subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)
        
        # Push to GitHub
        print("🚀 Pushing to GitHub...")
        result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Successfully pushed to GitHub!")
            print(f"🌐 Your repository: https://github.com/{username}/maa-kaali-bot")
            return True
        else:
            print(f"❌ Failed to push: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def show_deployment_options():
    """Show deployment options"""
    print("\n" + "=" * 50)
    print("🚀 STEP 3: Deploy Your Bot (FREE!)")
    print("=" * 50)
    print()
    print("Choose your deployment platform:")
    print()
    print("1. 🚂 Railway (Recommended - Easiest)")
    print("   - Go to: https://railway.app")
    print("   - Sign up with GitHub")
    print("   - Click 'New Project' → 'Deploy from GitHub repo'")
    print("   - Select your maa-kaali-bot repository")
    print()
    print("2. 🌐 Render (Alternative)")
    print("   - Go to: https://render.com")
    print("   - Sign up with GitHub")
    print("   - Click 'New' → 'Web Service'")
    print("   - Connect your repository")
    print()
    print("3. 🎨 Replit (For Development)")
    print("   - Go to: https://replit.com")
    print("   - Create new Python repl")
    print("   - Upload your files")
    print()
    
    choice = input("Which platform do you want to use? (1/2/3): ").strip()
    
    if choice == "1":
        webbrowser.open("https://railway.app")
        print("🚂 Opening Railway...")
    elif choice == "2":
        webbrowser.open("https://render.com")
        print("🌐 Opening Render...")
    elif choice == "3":
        webbrowser.open("https://replit.com")
        print("🎨 Opening Replit...")
    else:
        print("Invalid choice. Opening Railway (recommended)...")
        webbrowser.open("https://railway.app")

def show_environment_variables():
    """Show environment variables to set"""
    print("\n" + "=" * 50)
    print("🔧 STEP 4: Set Environment Variables")
    print("=" * 50)
    print()
    print("In your deployment platform, add these environment variables:")
    print()
    print("BOT_TOKEN=YOUR_BOT_TOKEN_HERE")
    print("ADMIN_CHAT_ID=YOUR_ADMIN_CHAT_ID_HERE")
    print("SHOPIFY_STORE_DOMAIN=maakaalicreations")
    print("SHOPIFY_API_ACCESS_TOKEN=YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE")
    print()
    print("💡 These are already configured in your bot code!")

def main():
    """Main function"""
    print_banner()
    
    # Check git status
    if not check_git_status():
        print("\n❌ Please run these commands first:")
        print("git init")
        print("git add .")
        print("git commit -m 'Initial commit'")
        return
    
    # Get GitHub username
    username = get_github_username()
    if not username:
        print("❌ Username is required!")
        return
    
    # Create GitHub repo instructions
    create_github_repo_instructions(username)
    
    # Push to GitHub
    if push_to_github(username):
        # Show deployment options
        show_deployment_options()
        
        # Show environment variables
        show_environment_variables()
        
        print("\n" + "=" * 50)
        print("🎉 CONGRATULATIONS!")
        print("=" * 50)
        print()
        print("Your bot is ready to deploy for FREE!")
        print()
        print("📱 Test your bot:")
        print("1. Open Telegram")
        print("2. Search for your bot")
        print("3. Send /start")
        print()
        print("📚 Read DEPLOYMENT.md for detailed instructions")
        print("📖 Read README.md for bot features and setup")
        print()
        print("🚀 Happy deploying!")
        
    else:
        print("\n❌ Failed to push to GitHub!")
        print("Please check your GitHub repository URL and try again.")

if __name__ == "__main__":
    main() 