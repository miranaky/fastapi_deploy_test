import uvicorn
from fastapi import FastAPI

# from app.routes.student import router as StudentRouter
from app.routes.file import router as FileRouter

app = FastAPI()
# app.include_router(StudentRouter, tags=["student"], prefix="/student")
app.include_router(FileRouter, tags=["file"], prefix="/dataset")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to fast api with mongodb"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
