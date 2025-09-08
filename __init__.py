from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/time")
async def time():
    from datetime import datetime
    return {"time": datetime.now().isoformat()}
