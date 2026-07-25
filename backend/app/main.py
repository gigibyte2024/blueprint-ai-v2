from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.blueprint import router as blueprint_router

app = FastAPI(title="Blueprint AI")

origins = [
    "http://localhost:5173",
    "https://blueprint-ai-v2-phi.vercel.app",  # replace if your Vercel URL is different
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blueprint_router)


@app.get("/")
def root():
    return {
        "message": "Blueprint AI Backend Running 🚀"
    }