from fastapi import APIRouter
from starlette.responses import JSONResponse

from . import predictions

temperature_model_pickle = r"Resources/TC_forecast.pkl"
polynomial_degree = 4

router = APIRouter()


@router.post('/temp')
@router.post('/temperature')
def temp_handler(post_body: dict) -> JSONResponse:
	features = list(map(int, post_body['days']))
	forecasts = predictions.predict(features=features, model_fp=temperature_model_pickle,
									polynomial_degree=polynomial_degree, formatter=lambda x: f"{x[0]} °C")
	return JSONResponse({f"Forecast for the day {k}": v for k, v in zip(features, forecasts)}, status_code=200)
