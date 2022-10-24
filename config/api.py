from ninja import NinjaAPI

from subjects.api import router as subjects_router

api = NinjaAPI(
    csrf=True,
    title="QP for All API",
    version="1.0.0",
    description="The official API of QP for All",
)

api.add_router("/subjects/", subjects_router)
