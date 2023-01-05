from django.contrib import admin

from .models import Curriculum, Paper, Qualification, Session, Subject

admin.site.register(Curriculum)
admin.site.register(Qualification)
admin.site.register(Session)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    list_filter = ["curriculums", "qualifications"]


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "id",
        "subject",
        "curriculum",
        "qualification",
        "session",
    ]
