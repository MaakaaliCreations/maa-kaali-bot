#!/usr/bin/env python3
"""
Test script to verify Shopify API connection
"""

import requests

# Your Shopify credentials
SHOPIFY_STORE_DOMAIN = "maakaalicreations"  # Try different variations
SHOPIFY_API_ACCESS_TOKEN = "YOUR_SHOPIFY_API_ACCESS_TOKEN_HERE"
SHOPIFY_API_VERSION = "2023-04"

def test_shopify_connection():
    """Test different Shopify domain variations"""
    
    possible_domains = [
        "maakaalicreations",
        "maakaalicreations.myshopify.com",
        "maakaalicreations.in",
        "maakaalicreations-in",
        "maakaalicreations-in.myshopify.com"
    ]
    
    headers = {
        'X-Shopify-Access-Token': SHOPIFY_API_ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }
    
    print("🔍 Testing Shopify API connections...\n")
    
    for domain in possible_domains:
        # Clean the domain
        if domain.endswith('.myshopify.com'):
            clean_domain = domain
        else:
            clean_domain = f"{domain}.myshopify.com"
        
        url = f"https://{clean_domain}/admin/api/{SHOPIFY_API_VERSION}/products.json"
        
        print(f"Testing: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                products_count = len(data.get('products', []))
                print(f"✅ SUCCESS! Found {products_count} products")
                print(f"✅ Correct domain: {clean_domain}")
                return clean_domain
            else:
                print(f"❌ Failed: {response.status_code}")
                if response.status_code == 401:
                    print("   → Unauthorized: Check your API token")
                elif response.status_code == 404:
                    print("   → Not found: Check store domain")
                elif response.status_code == 403:
                    print("   → Forbidden: Check API permissions")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("❌ No working connection found!")
    return None

def test_store_info():
    """Test getting store information"""
    working_domain = test_shopify_connection()
    
    if working_domain:
        print(f"\n🔍 Testing store info with: {working_domain}")
        
        headers = {
            'X-Shopify-Access-Token': SHOPIFY_API_ACCESS_TOKEN,
            'Content-Type': 'application/json'
        }
        
        # Test different endpoints
        endpoints = [
            "shop.json",
            "products.json?limit=1",
            "collections.json?limit=1",
            "blogs.json?limit=1"
        ]
        
        for endpoint in endpoints:
            url = f"https://{working_domain}/admin/api/{SHOPIFY_API_VERSION}/{endpoint}"
            
            try:
                response = requests.get(url, headers=headers, timeout=10)
                print(f"{endpoint}: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    if 'shop' in data:
                        print(f"   → Store: {data['shop'].get('name', 'Unknown')}")
                    elif 'products' in data:
                        print(f"   → Products: {len(data['products'])} found")
                    elif 'collections' in data:
                        print(f"   → Collections: {len(data['collections'])} found")
                    elif 'blogs' in data:
                        print(f"   → Blogs: {len(data['blogs'])} found")
                else:
                    print(f"   → Failed: {response.status_code}")
                    
            except Exception as e:
                print(f"{endpoint}: Error - {e}")
        
        return working_domain
    
    return None

if __name__ == "__main__":
    print("🧪 Shopify API Connection Test")
    print("=" * 40)
    
    working_domain = test_store_info()
    
    if working_domain:
        print(f"\n✅ SUCCESS! Use this domain in your bot:")
        print(f"SHOPIFY_STORE_DOMAIN = \"{working_domain.replace('.myshopify.com', '')}\"")
    else:
        print("\n❌ No working connection found!")
        print("\n🔧 Troubleshooting steps:")
        print("1. Check your Shopify API token permissions")
        print("2. Verify your store domain name")
        print("3. Make sure your app has the right scopes:")
        print("   - read_products")
        print("   - read_collections")
        print("   - read_articles")
        print("4. Check if your store is active") 