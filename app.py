from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
app = FastAPI(
    title="REST-API de usuarios con MongoDB",
    description="Base CRUD en fastAPI con base de datos en MongoDB",
    version="0.0.3",
    openapi_tags=tags_metadata
)

app.include_router(user)