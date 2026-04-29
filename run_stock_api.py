import sys
from pathlib import Path

# Add the 3_scalable_market_cap directory to the path
sys.path.insert(0, str(Path(__file__).parent / "3_scalable_market_cap"))

from api.stock_routes import app

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting FastAPI server...")
    print("📍 API URL: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
