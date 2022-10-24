from typing import List

from ninja import ModelSchema

from .models import Subject


class SubjectSchema(ModelSchema):
    curriculums: List[str]
    qualifications: List[str]

    class Config:
        model = Subject
        model_fields = "__all__"

    @staticmethod
    def resolve_curriculums(obj: Subject):
        return [curriculum.name for curriculum in obj.curriculums.all()]

    @staticmethod
    def resolve_qualifications(obj: Subject):
        return [
            qualification.name for qualification in obj.qualifications.all()
        ]
