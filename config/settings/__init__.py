from django.db.models import ForeignKey
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet


for cls in [QuerySet, BaseManager, ForeignKey]:
    cls.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls)


from .main import *


if DEBUG:
    from .local import *
else:
    from .production import *
