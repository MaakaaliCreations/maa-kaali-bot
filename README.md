# Maa Kaali Creations Telegram Bot

A fully functional Telegram bot for the Maa Kaali Creations Shopify store that allows customers to browse products, view offers, track orders, and get customer support.

<<<<<<< HEAD
**🚀 DEPLOYMENT STATUS: Updated for Render compatibility**

=======
>>>>>>> 269b789d4fc37c25a85f6f71f1336e0e327253b4
## Features

- 🛍 Browse saree collection with live Shopify data
- 💰 View current offers and discounts
- 🌟 Check new arrivals
- 📝 Place orders online
- ❓ Ask questions (forwarded to admin)
- 📦 Track orders
- 📰 View blog articles
- ☎️ Contact information
- 🎯 Inline keyboard navigation
- 🔄 Real-time Shopify API integration

## Prerequisites

- Python 3.8 or higher
- A Telegram bot token (from @BotFather)
- Shopify store with API access
- Admin chat ID for forwarding messages

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (you'll need this later)

### 3. Get Your Admin Chat ID

1. Send a message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Find your chat ID in the response

### 4. Create Shopify Private App

1. Log in to your Shopify admin panel
2. Go to **Apps** → **Develop apps** → **Create an app**
3. Give your app a name (e.g., "Telegram Bot")
4. Go to **API credentials** → **Admin API access token**
5. Select the following scopes:
   - `read_products`
   - `read_collections`
   - `read_articles`
   - `read_blog_articles`
6. Click **Install app**
7. Copy the **Admin API access token**

### 5. Configure the Bot

Edit `telegram_bot.py` and replace the following variables:

```python
# Bot Configuration
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # From @BotFather
ADMIN_CHAT_ID = "YOUR_ADMIN_CHAT_ID_HERE"  # Your chat ID

# Shopify Configuration
SHOPIFY_STORE_DOMAIN = "maakaalicreations.myshopify.com"  # Your store domain
SHOPIFY_API_ACCESS_TOKEN = "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE"  # From Shopify app

# Contact Information
CONTACT_INFO = {
    "phone": "+91-XXXXXXXXXX",  # Your phone number
    "whatsapp": "+91-XXXXXXXXXX",  # Your WhatsApp number
    "instagram": "https://instagram.com/maakaalicreations",  # Your Instagram
    "website": STORE_URL
}
```

## Running the Bot

### Local Development

```bash
python telegram_bot.py
```

### Deploy to Replit (Free)

1. Go to [replit.com](https://replit.com) and create an account
2. Click **Create Repl** → **Python**
3. Upload your `telegram_bot.py` and `requirements.txt` files
4. In the Replit shell, run:
   ```bash
   pip install -r requirements.txt
   ```
5. Click **Run** to start the bot

### Deploy to Railway (Free Tier)

1. Go to [railway.app](https://railway.app) and create an account
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard:
   - `BOT_TOKEN`
   - `ADMIN_CHAT_ID`
   - `SHOPIFY_STORE_DOMAIN`
   - `SHOPIFY_API_ACCESS_TOKEN`
4. Deploy automatically

## Environment Variables (Optional)

For better security, you can use environment variables instead of hardcoding values:

```python
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "YOUR_ADMIN_CHAT_ID_HERE")
SHOPIFY_STORE_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN", "maakaalicreations.myshopify.com")
SHOPIFY_API_ACCESS_TOKEN = os.getenv("SHOPIFY_API_ACCESS_TOKEN", "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE")
```

## Bot Commands

- `/start` - Show main menu
- `/help` - Show help information

## Menu Options

1. **🛍 Browse Saree Collection** - View products from Shopify
2. **💰 View Offers** - See current discounts and offers
3. **🌟 View New Arrivals** - Check latest products
4. **📝 Place an Order Online** - Direct link to store
5. **❓ Ask a Question** - Send questions to admin
6. **📦 Track My Order** - Order tracking assistance
7. **📰 View Blogs** - Latest blog articles
8. **☎️ Contact Us** - Contact information

## Customization

### Adding New Collections

To add support for specific collections, update the `find_collection_by_title()` function:

```python
def find_collection_by_title(title: str) -> Optional[str]:
    collections = fetch_collections()
    for collection in collections:
        if title.lower() in collection.get('title', '').lower():
            return str(collection['id'])
    return None
```

### Modifying Contact Information

Update the `CONTACT_INFO` dictionary in the configuration section:

```python
CONTACT_INFO = {
    "phone": "+91-XXXXXXXXXX",
    "whatsapp": "+91-XXXXXXXXXX", 
    "instagram": "https://instagram.com/maakaalicreations",
    "website": STORE_URL
}
```

### Changing Store URLs

Update the URL constants:

```python
STORE_URL = "https://maakaalicreations.in/"
TRACKING_URL = "https://maakaalicreations.in/apps/track123"
ALL_PRODUCTS_URL = "https://maakaalicreations.in/collections/all"
```

## Troubleshooting

### Common Issues

1. **Bot not responding**: Check if BOT_TOKEN is correct
2. **Shopify API errors**: Verify SHOPIFY_API_ACCESS_TOKEN and permissions
3. **Admin messages not working**: Ensure ADMIN_CHAT_ID is correct
4. **Products not showing**: Check if products are published in Shopify

### Debug Mode

Enable debug logging by modifying the logging level:

```python
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Change from INFO to DEBUG
)
```

## Security Notes

- Never commit your API tokens to version control
- Use environment variables for sensitive data
- Regularly rotate your Shopify API tokens
- Monitor bot usage and admin messages

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the Shopify API documentation
- Contact the bot admin through the bot itself

## License

This project is open source and available under the MIT License.

---

**Maa Kaali Creations** - Bringing traditional elegance to modern times 🎉 