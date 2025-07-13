#!/usr/bin/env python3
"""
Maa Kaali Creations Telegram Bot - Simplified Version
A fully functional bot for the Maa Kaali Creations Shopify store
"""

import os
import logging
import requests
from typing import Dict, List, Optional
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# =============================================================================
# CONFIGURATION
# =============================================================================

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "YOUR_ADMIN_CHAT_ID_HERE")

# Shopify Configuration
SHOPIFY_STORE_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN", "maakaalicreations")
SHOPIFY_API_ACCESS_TOKEN = os.getenv("SHOPIFY_API_ACCESS_TOKEN", "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE")

# Store URLs
STORE_URL = "https://maakaalicreations.in/"
ALL_PRODUCTS_URL = "https://maakaalicreations.in/collections/all"

# Contact Information
CONTACT_INFO = {
    "phone": "+91 9015132120, +91 6232133187",
    "whatsapp": "+91 8826137550, +91 6232133187",
    "email": "maakaalicreations@gmail.com",
    "instagram": "https://www.instagram.com/maakaali_creations/",
    "youtube": "https://www.youtube.com/@MaaKaali_Creations",
    "pinterest": "https://in.pinterest.com/maakaalicreations/",
    "facebook": "https://www.facebook.com/profile.php?id=61577363595465",
    "threads": "https://www.threads.com/@maakaali_creations",
    "twitter": "https://x.com/maakalicreation",
    "website": STORE_URL
}

# Brand Logo
BRAND_LOGO = "🪔"

# =============================================================================
# LOGGING SETUP
# =============================================================================

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# =============================================================================
# SHOPIFY API FUNCTIONS
# =============================================================================

def get_shopify_headers() -> Dict[str, str]:
    """Get headers for Shopify API requests"""
    return {
        'X-Shopify-Access-Token': SHOPIFY_API_ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }

def get_shopify_api_url(endpoint: str) -> str:
    """Generate Shopify API URL"""
    return f"https://{SHOPIFY_STORE_DOMAIN}.myshopify.com/admin/api/2023-04/{endpoint}"

def fetch_products(limit: int = 5) -> List[Dict]:
    """Fetch products from Shopify API"""
    try:
        url = get_shopify_api_url("products.json")
        params = {
            'limit': limit,
            'status': 'active'
        }
        
        response = requests.get(url, headers=get_shopify_headers(), params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data.get('products', [])
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        return []

# =============================================================================
# KEYBOARD CREATION FUNCTIONS
# =============================================================================

def create_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Create the main menu keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("🛍 Browse Saree Collection", callback_data="browse_collection"),
            InlineKeyboardButton("💰 View Offers", callback_data="view_offers")
        ],
        [
            InlineKeyboardButton("📝 Place an Order Online", callback_data="place_order")
        ],
        [
            InlineKeyboardButton("❓ Ask a Question", callback_data="ask_question"),
            InlineKeyboardButton("📰 View Blogs", callback_data="view_blogs")
        ],
        [
            InlineKeyboardButton("☎️ Contact Us", callback_data="contact_us"),
            InlineKeyboardButton("📱 Follow Us", callback_data="follow_us")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_back_to_menu_keyboard() -> InlineKeyboardMarkup:
    """Create back to menu keyboard"""
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]]
    return InlineKeyboardMarkup(keyboard)

# =============================================================================
# MESSAGE FORMATTING FUNCTIONS
# =============================================================================

def format_product_message(product: Dict) -> str:
    """Format a product for display"""
    title = product.get('title', 'Unknown Product')
    price = product.get('variants', [{}])[0].get('price', '0.00')
    url = f"{STORE_URL}products/{product.get('handle', '')}"
    
    message = f"*{title}*\n"
    message += f"💰 Price: ₹{price}\n"
    message += f"🔗 [View Product]({url})\n"
    
    return message

# =============================================================================
# COMMAND HANDLERS
# =============================================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command"""
    welcome_message = (
        f"{BRAND_LOGO} *Welcome to Maa Kaali Creations!* 🎉\n\n"
        "🌟 *Discover the beauty of traditional Indian sarees*\n\n"
        "✨ We offer a stunning collection of:\n"
        "• Designer Silk Sarees\n"
        "• Embroidered Net Sarees\n"
        "• Digital Printed Crepe Sarees\n"
        "• Kanjeevaram Silk Sarees\n"
        "• Twill Net Sarees with Sequin Work\n\n"
        "🛍 *Shop with confidence:*\n"
        "• Free shipping on all over India\n"
        "• Easy returns and exchanges\n"
        "• 24/7 customer support\n"
        "• Secure payment options\n\n"
    )
    
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown'
    )
    
    await update.message.reply_text(
        "Select an option:",
        reply_markup=create_main_menu_keyboard()
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command"""
    help_message = (
        f"{BRAND_LOGO} *Maa Kaali Creations Bot Help* 📚\n\n"
        "*Available Commands:*\n"
        "• /start - Show main menu\n"
        "• /help - Show this help message\n\n"
        "*Features:*\n"
        "• Browse our saree collection\n"
        "• View current offers and discounts\n"
        "• Place orders online\n"
        "• Ask questions\n"
        "• Read our blog articles\n"
        "• Contact us\n"
        "• Follow us on social media\n\n"
        "For any issues, contact our support team."
    )
    
    await update.message.reply_text(
        help_message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown'
    )

# =============================================================================
# CALLBACK QUERY HANDLERS
# =============================================================================

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle callback queries from inline keyboards"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "back_to_menu":
        await show_main_menu(query)
    elif query.data == "browse_collection":
        await browse_collection(query)
    elif query.data == "view_offers":
        await view_offers(query)
    elif query.data == "place_order":
        await place_order(query)
    elif query.data == "ask_question":
        await ask_question(query, context)
    elif query.data == "view_blogs":
        await view_blogs(query)
    elif query.data == "contact_us":
        await contact_us(query)
    elif query.data == "follow_us":
        await follow_us(query)

async def show_main_menu(query) -> None:
    """Show the main menu"""
    welcome_message = (
        f"{BRAND_LOGO} *Maa Kaali Creations* 🎉\n\n"
        "Choose an option from the menu below:"
    )
    await query.edit_message_text(
        welcome_message,
        reply_markup=create_main_menu_keyboard(),
        parse_mode='Markdown'
    )

async def browse_collection(query) -> None:
    """Handle browse collection request"""
    await query.edit_message_text(
        f"{BRAND_LOGO} *🛍 Fetching our saree collection...*",
        parse_mode='Markdown'
    )
    
    products = fetch_products(limit=5)
    
    if not products:
        # Fallback to static product list
        message = (
            f"{BRAND_LOGO} *🛍 Our Saree Collection*\n\n"
            f"{BRAND_LOGO} *Featured Products:*\n\n"
            f"{BRAND_LOGO} *1.* **Aqua Blue Embroidered Twill Net Saree**\n"
            "💰 Price: ₹385 (Sale from ₹925)\n"
            "🔗 [View Product](https://maakaalicreations.in/products/aqua-blue-embroidered-twill-net-saree-with-running-blouse)\n\n"
            
            f"{BRAND_LOGO} *2.* **Beautiful Digital Printed Crepe Silk Saree**\n"
            "💰 Price: ₹405 (Sale from ₹1,005)\n"
            "🔗 [View Product](https://maakaalicreations.in/products/beautiful-digital-printed-crepe-silk-saree)\n\n"
            
            f"{BRAND_LOGO} *3.* **Crimson Bloom Net Saree with Embroidered Work**\n"
            "💰 Price: ₹345 (Sale from ₹1,025)\n"
            "🔗 [View Product](https://maakaalicreations.in/products/crimson-bloom-net-saree-with-embroidered-work)\n\n"
            
            f"{BRAND_LOGO} *4.* **Designer Kanjeevaram Silk Saree**\n"
            "💰 Price: ₹515\n"
            "🔗 [View Product](https://maakaalicreations.in/products/designer-kanjeevaram-silk-saree-with-golden-zari-work)\n\n"
            
            f"{BRAND_LOGO} *5.* **Designer Twill Net Saree with Sequin Work**\n"
            "💰 Price: ₹655 (Sale from ₹1,825)\n"
            "🔗 [View Product](https://maakaalicreations.in/products/designer-twill-net-saree-with-shimmering-sequin-all-over)\n\n"
            
            f"*View all products:* {ALL_PRODUCTS_URL}"
        )
    else:
        message = f"{BRAND_LOGO} *🛍 Our Saree Collection*\n\n"
        for i, product in enumerate(products, 1):
            message += f"*{i}.* {format_product_message(product)}\n"
        message += f"\n*View all products:* {ALL_PRODUCTS_URL}"
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def view_offers(query) -> None:
    """Handle view offers request"""
    message = (
        f"{BRAND_LOGO} *💰 Special Offers*\n\n"
        "🎁 *EXCLUSIVE DISCOUNTS FOR YOU!*\n\n"
        "🔥 *Get Up To 5% OFF*\n"
        "• On prepaid orders\n"
        "• Minimum purchase of ₹300.00\n"
        "• Automatic discount applied\n\n"
        "🎯 *Up To 25% OFF*\n"
        "• For first purchase only\n"
        "• New customers exclusive\n"
        "• One-time use per customer\n"
        "• Use code: `SAVE25`\n\n"
        "🚚 *FREE SHIPPING*\n"
        "• Free shipping on all orders\n"
        "• No minimum purchase required\n"
        "• Fast and reliable delivery\n\n"
        "💎 *Premium Silk Sarees* at affordable prices\n"
        "✨ *Limited time offers - Shop now!*\n\n"
        f"*Shop now:* {ALL_PRODUCTS_URL}"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def place_order(query) -> None:
    """Handle place order request"""
    message = (
        f"{BRAND_LOGO} *📝 Place an Order Online*\n\n"
        "Ready to shop? Visit our online store to browse our complete collection!\n\n"
        "🛒 *Features:*\n"
        "• Secure payment options\n"
        "• Free shipping on orders above ₹999\n"
        "• Easy returns and exchanges\n"
        "• 24/7 customer support\n\n"
        f"*🛍 Shop Now:* {STORE_URL}\n\n"
        "💡 *Tip:* Use code `MKC15` for 15% off!"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown'
    )

async def ask_question(query, context) -> None:
    """Handle ask question request"""
    context.user_data['waiting_for_question'] = True
    
    message = (
        f"{BRAND_LOGO} *❓ Ask a Question*\n\n"
        "Have a question about our products or services?\n\n"
        "Simply type your question below and we'll get back to you soon!\n\n"
        "📝 *You can ask about:*\n"
        "• Product details and availability\n"
        "• Sizing and measurements\n"
        "• Shipping and delivery\n"
        "• Returns and exchanges\n"
        "• Payment options\n"
        "• Any other queries\n\n"
        "💡 *Just type your question in the chat below!*"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown'
    )

async def view_blogs(query) -> None:
    """Handle view blogs request"""
    message = (
        f"{BRAND_LOGO} *📰 Latest Blog Articles*\n\n"
        f"{BRAND_LOGO} *1.* **Why Fast Fashion's Impact on the Environment is a Big Deal**\n"
        "📅 July 9, 2025\n"
        "In recent years, the fashion industry has come under significant scrutiny for its role in environmental degradation...\n"
        "🔗 [Read More](https://maakaalicreations.in/blogs/news/why-fast-fashions-impact-on-the-environment-is-a-big-deal)\n\n"
        
        f"{BRAND_LOGO} *2.* **How to Identify Quality Fabrics for Your Wardrobe**\n"
        "📅 June 30, 2025\n"
        "Selecting the right fabrics for your wardrobe is not just an essential skill for fashion enthusiasts but also for anyone who desires durable and stylish clothing...\n"
        "🔗 [Read More](https://maakaalicreations.in/blogs/news/how-to-identify-quality-fabrics-for-your-wardrobe)\n\n"
        
        f"{BRAND_LOGO} *3.* **The Art of Saree Draping: Traditional Techniques**\n"
        "📅 June 15, 2025\n"
        "Discover the beautiful art of saree draping with traditional techniques that have been passed down through generations...\n"
        "🔗 [Read More](https://maakaalicreations.in/blogs/news/the-art-of-saree-draping)\n\n"
        
        f"*Visit our blog:* {STORE_URL}blogs/news"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def contact_us(query) -> None:
    """Handle contact us request"""
    message = (
        f"{BRAND_LOGO} 📞 Contact Us\n\n"
        "Get in touch with us through any of these channels:\n\n"
        f"📱 Call: {CONTACT_INFO['phone']}\n"
        f"💬 WhatsApp: {CONTACT_INFO['whatsapp']}\n"
        f"📧 Email: {CONTACT_INFO['email']}\n"
        f"🌐 Website: {CONTACT_INFO['website']}\n\n"
        "📱 Social Media:\n"
        f"• Instagram: {CONTACT_INFO['instagram']}\n"
        f"• YouTube: {CONTACT_INFO['youtube']}\n"
        f"• Facebook: {CONTACT_INFO['facebook']}\n"
        f"• Twitter/X: {CONTACT_INFO['twitter']}\n"
        f"• Pinterest: {CONTACT_INFO['pinterest']}\n"
        f"• Threads: {CONTACT_INFO['threads']}\n\n"
        "🕒 Business Hours:\n"
        "24/7 Available - You can reach out to us anytime!\n\n"
        "💝 We're here to help!"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode=None,
        disable_web_page_preview=True
    )

async def follow_us(query) -> None:
    """Handle follow us request"""
    message = (
        f"{BRAND_LOGO} 📱 Follow Us\n\n"
        "Stay connected with us on social media for the latest updates, new arrivals, and exclusive offers!\n\n"
        "🌟 Our Social Media:\n"
        f"• Instagram: {CONTACT_INFO['instagram']}\n"
        f"• YouTube: {CONTACT_INFO['youtube']}\n"
        f"• Facebook: {CONTACT_INFO['facebook']}\n"
        f"• Twitter/X: {CONTACT_INFO['twitter']}\n"
        f"• Pinterest: {CONTACT_INFO['pinterest']}\n"
        f"• Threads: {CONTACT_INFO['threads']}\n\n"
        "🎯 Don't miss out on our latest updates!"
    )
    
    await query.edit_message_text(
        message,
        reply_markup=create_back_to_menu_keyboard(),
        parse_mode=None,
        disable_web_page_preview=True
    )

# =============================================================================
# MESSAGE HANDLERS
# =============================================================================

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages from users"""
    user = update.message.from_user
    text = update.message.text
    
    # Check if user is waiting for a question
    if context.user_data.get('waiting_for_question'):
        admin_message = (
            f"{BRAND_LOGO} *❓ New Question from User*\n\n"
            f"*User:* {user.first_name} (@{user.username})\n"
            f"*User ID:* {user.id}\n"
            f"*Question:* {text}"
        )
        
        # Send to admin
        try:
            await context.bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                text=admin_message,
                parse_mode='Markdown'
            )
            
            # Confirm to user
            await update.message.reply_text(
                f"{BRAND_LOGO} *✅ Question Received!*\n\n"
                "Thank you for your question. We'll get back to you soon!\n\n"
                "In the meantime, feel free to browse our collection.",
                reply_markup=create_back_to_menu_keyboard(),
                parse_mode='Markdown'
            )
        except Exception as e:
            logger.error(f"Error sending message to admin: {e}")
            await update.message.reply_text(
                f"{BRAND_LOGO} *❌ Error*\n\n"
                "Sorry, there was an error sending your question. "
                "Please try again later or contact us directly.",
                reply_markup=create_back_to_menu_keyboard(),
                parse_mode='Markdown'
            )
        
        context.user_data.pop('waiting_for_question', None)
        return
    
    # Default response for any other text
    await update.message.reply_text(
        f"{BRAND_LOGO} *🤖 Maa Kaali Creations Bot*\n\n"
        "Use the menu below to navigate or type /start to see all options.",
        reply_markup=create_main_menu_keyboard(),
        parse_mode='Markdown'
    )

# =============================================================================
# MAIN APPLICATION SETUP
# =============================================================================

def main() -> None:
    """Start the bot"""
    # Validate environment variables
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Error: BOT_TOKEN not set. Please set the BOT_TOKEN environment variable.")
        return
    
    if ADMIN_CHAT_ID == "YOUR_ADMIN_CHAT_ID_HERE":
        print("❌ Error: ADMIN_CHAT_ID not set. Please set the ADMIN_CHAT_ID environment variable.")
        return
    
    if SHOPIFY_API_ACCESS_TOKEN == "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE":
        print("❌ Error: SHOPIFY_API_ACCESS_TOKEN not set. Please set the SHOPIFY_API_ACCESS_TOKEN environment variable.")
        return
    
    try:
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        
        # Add callback query handler
        application.add_handler(CallbackQueryHandler(handle_callback_query))
        
        # Add message handler for text messages
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
        
        # Start the bot
        print("🤖 Maa Kaali Creations Bot is starting...")
        print("📱 Bot is now running. Press Ctrl+C to stop.")
        
        # Use polling with proper conflict handling
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                application.run_polling(drop_pending_updates=True, close_loop=False)
                break
            except Exception as e:
                if "Conflict" in str(e) and retry_count < max_retries - 1:
                    retry_count += 1
                    print(f"⚠️ Bot conflict detected (attempt {retry_count}/{max_retries}). Waiting 10 seconds and retrying...")
                    import time
                    time.sleep(10)
                else:
                    raise e
        
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("Please check your environment variables and try again.")

if __name__ == '__main__':
    main() 