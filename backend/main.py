from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import patients, entries, auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mood and Pain Tracker API",
    description="API for tracking patient mood and pain levels",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],  # Next.js development server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(patients.router, prefix="/api/patients", tags=["patients"])
app.include_router(entries.router, prefix="/api/entries", tags=["entries"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Mood and Pain Tracker API"}

@app.get("/api/ping")
async def ping():
    return {"message": "pong"}

@app.get("/api/db-status")
async def db_status():
    return {"message": "Database connected", "tables_created": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)