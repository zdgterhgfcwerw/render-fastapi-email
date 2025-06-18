from fastapi import FastAPI, Request
from typing import List
import uvicorn
import os

app = FastAPI()

# 메일 저장용 리스트
email_queue: List[dict] = []

@app.post("/send_email")
async def send_email(request: Request):
    data = await request.json()
    print("받은 이메일 데이터:", data)
    email_queue.append(data)
    return {"status": "queued", "queued_count": len(email_queue)}

@app.get("/get_email")
async def get_email():
    if email_queue:
        return email_queue.pop(0)
    return {"status": "empty"}

# 실행 코드
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
