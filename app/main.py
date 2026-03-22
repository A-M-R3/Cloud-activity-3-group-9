from fastapi import FastAPI
from app.authentication.router import router as auth_router
from app.files.router import router as files_router
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM


app = FastAPI()

app.include_router(auth_router, prefix="/authentication", tags=["Authentication"])
app.include_router(files_router, prefix="/files", tags=["Files"])

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)