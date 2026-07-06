import uvicorn
from fastapi import File, UploadFile, Request, FastAPI, HTTPException

app = FastAPI()

@app.post("/docx")
async def docx():
    return {"message": "Testdocx"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
