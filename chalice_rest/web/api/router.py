from fastapi.routing import APIRouter

from chalice_rest.web.api import docs, echo, kafka, monitoring, rabbit, redis

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
api_router.include_router(rabbit.router, prefix="/rabbit", tags=["rabbit"])
api_router.include_router(kafka.router, prefix="/kafka", tags=["kafka"])
