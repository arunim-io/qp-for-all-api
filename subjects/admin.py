from django.contrib import admin

from .models import Curriculum, Paper, Qualification, Session, Subject

admin.site.register(Curriculum)
admin.site.register(Qualification)
admin.site.register(Session)
admin.site.register(Subject)
admin.site.register(Paper)
