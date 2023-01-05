from ninja import NinjaAPI

from api.router import router as subjects_router

api = NinjaAPI(
    csrf=True,
    title="QP for All API",
    version="1.0.0",
    description="The official API of QP for All",
)

api.add_router("/", subjects_router)
