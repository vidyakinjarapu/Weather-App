from fastapi import FastAPI

app = FastAPI(title = "WeatherApp")

@app.get('/')
def root():
    return {"mesasge" : "Hello! Weather app is running!"}

@app.get("/health")
def health():
    return {"status" : "ok"}