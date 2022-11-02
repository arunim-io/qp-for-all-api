from typing import List

from ninja import Router

from django.shortcuts import get_object_or_404

from .models import Paper, Subject
from .schemas import SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(request, query: str = ""):
    """
    Get a list of subjects.
    """

    return (
        Subject.objects.filter(name=query.capitalize())
        if query
        else Subject.objects.all()
    )


@router.get("/{subject_id}/", response=SubjectSchema)
def get_subject(
    request, subject_id: int, curriculum: str = "", qualification: str = ""
):
    """
    Get a subject by id.
    """

    if curriculum:
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
