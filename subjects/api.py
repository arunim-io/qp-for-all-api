from typing import List

from ninja import Router

from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .models import Subject
from .schemas import SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(
    request: HttpRequest, curriculum: str = "", qualification: str = ""
):
    """
    Get a list of subjects.
    """

    filters = Q()

    if curriculum != "":
        filters &= Q(curriculums__name=curriculum)
    if qualification != "":
        filters &= Q(qualifications__name=qualification)

    return Subject.objects.filter(filters)


@router.get("/{pk}/", response=SubjectSchema)
def get_subject(
    request: HttpRequest,
    pk: int,  # pylint: disable=C0103
    curriculum: str = "",
    qualification: str = "",
):
    """
    Get a subject by id.
    """

    filters = Q(pk=pk)

    if curriculum != "":
        filters &= Q(papers__curriculums__name=curriculum)
    if qualification != "":
        filters &= Q(papers__qualifications__name=qualification)

    return get_object_or_404(Subject, filters)
