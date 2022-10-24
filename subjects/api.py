from typing import List

from django.http import HttpRequest
from ninja import Router

from .models import Subject
from .schemas import SubjectSchema

router = Router()


@router.get("/", response=List[SubjectSchema])
def get_subjects(request: HttpRequest):
    return Subject.objects.filter(qualifications__name__contains="IAS")
