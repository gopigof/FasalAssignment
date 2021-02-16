from fastapi import APIRouter
from starlette.responses import JSONResponse

from . import predictions

humidity_model_pickle = r"Resources/HUM_forecast.pkl"
polynomial_degree = 3

router = APIRouter()


@router.post('/humidity')
@router.post('/hum')
def hum_handler(post_body: dict) -> JSONResponse:
	features = list(map(int, post_body['days']))
	forecasts = predictions.predict(features=features, model_fp=humidity_model_pickle,
									polynomial_degree=polynomial_degree, formatter=lambda x: f"{x[0]} %")
	return JSONResponse({f"Forecast for day {k}": v for k, v in zip(features, forecasts)}, status_code=200)
