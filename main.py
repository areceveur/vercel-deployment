from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import get_db , engine , Base
import os
import uvicorn
from newsletter.routes import router as newsletter_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(newsletter_route)
@app.get("/")
@app.head("/")

async def root():
    return {
        "status": "ok", 
        "service": "newsletter-api",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
@app.head("/health")

async def health_check():
    return {
        "status": "ok", 
        "service": "newsletter-api",
        "timestamp": datetime.utcnow().isoformat()
    }


Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=[os.path.dirname(os.path.abspath(__file__))],
        reload_excludes=[
            "*/.git/*",
            "*/__pycache__/*",
            "*.pyc",
            "*/.pytest_cache/*",
            "*/.vscode/*",
            "*/.idea/*"
        ],
        reload_delay=1,
        reload_includes=["*.py", "*.html", "*.css", "*.js"]
    )