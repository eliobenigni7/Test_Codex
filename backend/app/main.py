from fastapi import FastAPI

from .routers import apps, costs

app = FastAPI(title="IT Financials SaaS")

app.include_router(apps.router, prefix="/v1/apps", tags=["apps"])
app.include_router(costs.router, prefix="/v1/costs", tags=["costs"])
