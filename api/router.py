from typing import List

from ninja import Router

from django.shortcuts import get_object_or_404

from .models import Paper, Session, Subject
from .schemas import PaperSchema, SessionSchema, SubjectSchema

router = Router()


@router.get("/subjects/", response=List[SubjectSchema])
def get_subjects(_, query: str = ""):
    """Get a list of subjects"""

    return (
        Subject.objects.filter(name__icontains=query)
        if query
        else Subject.objects.all()
    )


@router.get("/subjects/{subject_id}/", response=SubjectSchema)
def get_subject(_, subject_id: int, curriculum="", qualification="", query=""):
    """Get a subject by id"""

    if query:
        if curriculum:
            if qualification:
                if Paper.objects.filter(
                    subject__id=subject_id,
                    curriculum__name=curriculum,
                    qualification__name=qualification,
                    session__name__icontains=query,
                ).exists():
                    return get_object_or_404(
                        Subject,
                        id=subject_id,
                        curriculums__name=curriculum,
                        qualifications__name=qualification,
                        papers__curriculum__name=curriculum,
                        papers__qualification__name=qualification,
                        sessions__name__icontains=query,
                    )

                return get_object_or_404(
                    Subject,
                    id=subject_id,
                    curriculums__name=curriculum,
                    qualifications__name=qualification,
                    sessions__name__icontains=query,
                )

            if Paper.objects.filter(
                subject__id=subject_id,
                curriculum__name=curriculum,
                session__name__icontains=query,
            ).exists():
                return get_object_or_404(
                    Subject,
                    id=subject_id,
                    curriculums__name=curriculum,
                    papers__curriculum__name=curriculum,
                    sessions__name__icontains=query,
                )

            return get_object_or_404(
                Subject,
                id=subject_id,
                curriculums__name=curriculum,
                sessions__name__icontains=query,
            )

        if qualification:
            return (
                get_object_or_404(
                    Subject,
                    id=subject_id,
                    qualifications__name=qualification,
                    papers__qualification__name=qualification,
                    sessions__name__icontains=query,
                )
                if Paper.objects.filter(
                    subject__id=subject_id,
                    qualification__name=qualification,
                    session__name__icontains=query,
                ).exists()
                else get_object_or_404(
                    Subject,
                    id=subject_id,
                    qualifications__name=qualification,
                    sessions__name__icontains=query,
                )
            )
        else:
            return get_object_or_404(
                Subject,
                id=subject_id,
                sessions__name__icontains=query,
            )

    elif curriculum:
        if qualification:
            if Paper.objects.filter(
                subject__id=subject_id,
                curriculum__name=curriculum,
                qualification__name=qualification,
            ).exists():
                return get_object_or_404(
                    Subject,
                    id=subject_id,
                    curriculums__name=curriculum,
                    qualifications__name=qualification,
                    papers__curriculum__name=curriculum,
                    papers__qualification__name=qualification,
                )

            return get_object_or_404(
                Subject,
                id=subject_id,
                curriculums__name=curriculum,
                qualifications__name=qualification,
            )

        if Paper.objects.filter(
            subject__id=subject_id, curriculum__name=curriculum
        ).exists():
            return get_object_or_404(
                Subject,
                id=subject_id,
                curriculums__name=curriculum,
                papers__curriculum__name=curriculum,
            )

        return get_object_or_404(
            Subject, id=subject_id, curriculums__name=curriculum
        )

    if not qualification:
        return get_object_or_404(Subject, id=subject_id)

    return (
        get_object_or_404(
            Subject,
            id=subject_id,
            qualifications__name=qualification,
            papers__qualification__name=qualification,
        )
        if Paper.objects.filter(
            subject__id=subject_id, qualification__name=qualification
        ).exists()
        else get_object_or_404(
            Subject, id=subject_id, qualifications__name=qualification
        )
    )


@router.get("/sessions/", response=List[SessionSchema])
def get_sessions(_):
    return Session.objects.all()


@router.get("/sessions/{session_id}", response=SessionSchema)
def get_session(_, session_id: int):
    return Session.objects.get(id=session_id)


@router.get("/papers/", response=List[PaperSchema])
def get_papers(_):
    return Paper.objects.all()


@router.get("/papers/{paper_id}", response=PaperSchema)
def get_paper(_, paper_id: int):
    return Paper.objects.get(id=paper_id)
