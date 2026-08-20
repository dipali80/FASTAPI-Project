
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routs_auth, routs_predict
from app.middleware.login_middleware import LoggingMiddleware
from app.core.exceptions import registor_exception_handlers

app = FastAPI(title='Car Price Prediction')

# link middleware

app.add_middleware(LoggingMiddleware)

#link endpoints

app.include_router(routs_auth.router, tags=['auth'])
app.include_router(routs_predict.router, tags=['prediction'])

