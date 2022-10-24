from ninja import NinjaAPI

from subjects.api import router as subjects_router

api = NinjaAPI()

api.add_router("/subjects/", subjects_router)
