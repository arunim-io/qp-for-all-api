from typing import List

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Subject
from .schemas import SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(request: HttpRequest):
    return Subject.objects.filter(qualifications__name__contains="IAS")


@router.get("/{id}", response=SubjectSchema)
def get_subject(request: HttpRequest, id: int):
    return get_object_or_404(Subject, id=id)
