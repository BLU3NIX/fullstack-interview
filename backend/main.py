from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todos import router as todos_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["Content-Type", "X-API-Key"],
)

# Include routers
app.include_router(todos_router)
