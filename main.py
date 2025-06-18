from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/send_email")
async def send_email(request: Request):
    data = await request.json()
    print("받은 이메일 데이터:", data)
    return {"status": "ok"}
