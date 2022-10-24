from typing import List

from ninja import ModelSchema
from ninja.orm import create_schema

from .models import Paper, Session, Subject

SessionSchema = create_schema(Session)


class PaperSchema(ModelSchema):
    subject: str
    curriculum: str
    qualification: str
    session: str

    class Config:
        model = Paper
        model_fields = "__all__"

    @staticmethod
    def resolve_subject(obj: Paper):
        return obj.subject.name

    @staticmethod
    def resolve_curriculum(obj: Paper):
        return obj.curriculum.name

    @staticmethod
    def resolve_qualification(obj: Paper):
        return obj.qualification.name

    @staticmethod
    def resolve_session(obj: Paper):
        return obj.session.name


class SubjectSchema(ModelSchema):
    curriculums: List[str]
    qualifications: List[str]
    sessions: List[SessionSchema]  # type: ignore
    papers: List[PaperSchema]  # type: ignore

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

    @staticmethod
    def resolve_papers(obj: Subject):
        return Paper.objects.filter(subject__id=obj.id)  # type: ignore
