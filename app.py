from fastapi import FastAPI
from router import humidity_predictor_router, temperature_predictor_router

app = FastAPI()
app.include_router(humidity_predictor_router.router, prefix='/predict')
app.include_router(temperature_predictor_router.router, prefix='/predict')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Micro-climate Predictor up and running!'
