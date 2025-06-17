from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/send_email")
async def receive_email(request: Request):
    data = await request.json()
    print("📩 GPTs가 보낸 이메일:")
    print("To:", data.get("to"))
    print("Subject:", data.get("subject"))
    print("Body:", data.get("body"))
    return {"status": "received"}
