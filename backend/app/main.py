from fastapi import FastAPI

app = FastAPI(
    title="Blueprint AI Backend",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Blueprint AI Backend Running 🚀"}