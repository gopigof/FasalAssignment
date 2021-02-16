import pickle
from typing import List, Callable

import numpy as np
from sklearn.preprocessing import PolynomialFeatures


def predict(features: List[int], model_fp: str, polynomial_degree: int, formatter: Callable) -> List[str]:
	linear_model = pickle.load(open(model_fp, 'rb'))
	predictors = np.asarray(features).reshape((-1, 1))
	predictor_variables = PolynomialFeatures(degree=polynomial_degree).fit_transform(predictors)
	forecasts = linear_model.predict(predictor_variables)
	return list(map(formatter, forecasts))
