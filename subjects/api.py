from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Subject
from .schemas import SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(request: HttpRequest):
    """
    Get a list of subjects.
    """

    return Subject.objects.filter(qualifications__name__contains="IAS")


@router.get("/{subject_id}", response=SubjectSchema)
def get_subject(request: HttpRequest, subject_id: int):
    """
    Get a subject by id.
    """

    return get_object_or_404(Subject, id=subject_id)
