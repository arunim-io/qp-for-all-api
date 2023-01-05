from typing import List

from ninja import ModelSchema

from django.conf import settings

from .models import Paper, Session, Subject


class PaperSchema(ModelSchema):
    subject: str
    curriculum: str
    qualification: str
    session: str
    qp_url: str
    ms_url: str

    class Config:
        model = Paper
        model_fields = "__all__"
        model_exclude = ["question_paper", "mark_scheme"]

    @staticmethod
    def resolve_subject(obj: Paper) -> str:
        return obj.subject.name

    @staticmethod
    def resolve_curriculum(obj: Paper) -> str:
        return obj.curriculum.name

    @staticmethod
    def resolve_qualification(obj: Paper) -> str:
        return obj.qualification.name

    @staticmethod
    def resolve_session(obj: Paper) -> str:
        return obj.session.name

    @staticmethod
    def resolve_qp_url(obj: Paper) -> str:
        return obj.question_paper.url

    @staticmethod
    def resolve_ms_url(obj: Paper) -> str:
        return obj.mark_scheme.url


class SessionSchema(ModelSchema):
    papers: List[PaperSchema]

    class Config:
        model = Session
        model_fields = "__all__"

    @staticmethod
    def resolve_papers(obj: Session):
        return Paper.objects.filter(session__id=obj.id)


class SubjectSchema(ModelSchema):
    curriculums: List[str]
    qualifications: List[str]
    sessions: List[SessionSchema]
    papers: List[PaperSchema]

    class Config:
        model = Subject
        model_fields = "__all__"

    @staticmethod
    def resolve_curriculums(obj: Subject) -> List[str]:
        return [curriculum.name for curriculum in obj.curriculums.all()]

    @staticmethod
    def resolve_qualifications(obj: Subject) -> List[str]:
        return [
            qualification.name for qualification in obj.qualifications.all()
        ]

    @staticmethod
    def resolve_papers(obj: Subject):
        return Paper.objects.filter(subject__id=obj.id)
