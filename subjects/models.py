from django.db import models


class Curriculum(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculums"

    def __str__(self) -> str:
        return self.name


class Qualification(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    curriculums = models.ManyToManyField(
        Curriculum, related_name="curriculums"
    )
    qualifications = models.ManyToManyField(
        Qualification, related_name="qualifications"
    )

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self) -> str:
        return self.name
