from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from src.api.v1.routers import router as v1_api_router
app = FastAPI()


origins = [
    "*"
]



# Apply CORS middleware first
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_api_router, prefix="/api/v1")
