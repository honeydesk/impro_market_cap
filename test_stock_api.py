import requests
import json

# Test the FastAPI endpoint
url = "http://localhost:8000/market-cap"

payload = {
    "symbol": "AAPL",
    "price_per_share": 150.25,
    "total_shares": 1000000
}

print("📤 Sending request to", url)
print("📋 Payload:", json.dumps(payload, indent=2))

try:
    response = requests.post(url, json=payload)
    
    print("\n✅ Response Status:", response.status_code)
    print("📥 Response Data:")
    print(json.dumps(response.json(), indent=2))
    
except requests.exceptions.ConnectionError:
    print("❌ Error: Could not connect to FastAPI server.")
    print("Make sure to run: python run_stock_api.py")
except Exception as e:
    print(f"❌ Error: {e}")
