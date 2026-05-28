import httpx
from contextlib import asynccontextmanager  
from fastapi import FastAPI, Request, HTTPException

@asynccontextmanager
async def lifespan(app: FastAPI):
    #runs on startup
    app.state.http_client = httpx.AsyncClient(timeout=10.0)
    yield
    #runs on shutdown
    await app.state.http_client.aclose()

app = FastAPI(title = "WeatherApp", lifespan=lifespan)


@app.get('/')
def root():
    return {"mesasge" : "Hello! Weather app is running!"}

@app.get("/health")
def health():
    return {"status" : "ok"}

@app.get("/weather")
async def get_weather(request: Request, city: str):
    client = request.app.state.http_client

    # Getting the coordinates of the city -> lat, log
    geo_resp = await client.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params = {"name": city, "count": 1}
    )

    geo_data = geo_resp.json()

    if not geo_data.get("results"):
        raise HTTPException(status_code=404, detail=f"city '{city} not found!")
    
    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]

    # Getting current weather using those coordinates
    weather_resp = await client.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current_weather": True},
    )
    weather = weather_resp.json()["current_weather"]

    return {
        "city": location["name"],
        "country": location.get("country"),
        "temperature_c": weather["temperature"],
        "windspeed_kmh": weather["windspeed"],
        "weather_code": weather["weathercode"]
    }

