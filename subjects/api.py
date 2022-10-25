from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Subject
from .schemas import SessionSchema, SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(request: HttpRequest, curriculum: str = ""):
    """
    Get a list of subjects.
    """

    return Subject.objects.filter(curriculums__name__contains=curriculum)


@router.get("/{subject_id}", response=SubjectSchema)
def get_subject(request: HttpRequest, subject_id: int):
    """
    Get a subject by id.
    """

    return get_object_or_404(Subject, id=subject_id)


@router.get("/{subject_id}/sessions/", response=List[SessionSchema])
def get_sessions(request: HttpRequest, subject_id: int):
    """
    Get a list of sessions for a subject.
    """

    return get_object_or_404(Subject, id=subject_id).sessions
