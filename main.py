from fastapi import FastAPI, Request
import uvicorn
import os

app = FastAPI()

@app.post("/send_email")
async def send_email(request: Request):
    data = await request.json()
    print("받은 이메일 데이터:", data)
    return {"status": "ok"}

# 실행 코드 추가
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render가 요구하는 포트 사용
    uvicorn.run("main:app", host="0.0.0.0", port=port)
