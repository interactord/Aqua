from fastapi import APIRouter, FastAPI

app = FastAPI()
# app.include_router(classifier.router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
async def root():
    return {"message": "hello world"}