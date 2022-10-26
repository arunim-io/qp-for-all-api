from django.db import models


class Curriculum(models.Model):
    id: int
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculums"

    def __str__(self) -> str:
        return self.name


class Qualification(models.Model):
    id: int
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"

    def __str__(self) -> str:
        return self.name


class Session(models.Model):
    id: int
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self):
        return self.name


class Subject(models.Model):
    id: int
    name = models.CharField(max_length=255)
    curriculums = models.ManyToManyField(
        Curriculum, related_name="curriculums"
    )
    qualifications = models.ManyToManyField(
        Qualification, related_name="qualifications"
    )
    sessions = models.ManyToManyField(Session, related_name="sessions")
    papers = models.ManyToManyField("Paper", related_name="papers")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self) -> str:
        return self.name


class Paper(models.Model):
    id: int
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(
        Subject, related_name="subject", on_delete=models.CASCADE
    )
    curriculum = models.ForeignKey(
        Curriculum, related_name="curriculum", on_delete=models.CASCADE
    )
    qualification = models.ForeignKey(
        Qualification, related_name="qualification", on_delete=models.CASCADE
    )
    session = models.ForeignKey(
        Session, related_name="session", on_delete=models.CASCADE
    )
    qp_url = models.URLField(max_length=255)
    ms_url = models.URLField(max_length=255)

    class Meta:
        verbose_name = "Paper"
        verbose_name_plural = "Papers"

    def __str__(self) -> str:
        return self.title
