from fastapi import FastAPI

from Controller import app as customer_router
app = FastAPI()
app.include_router(customer_router)
