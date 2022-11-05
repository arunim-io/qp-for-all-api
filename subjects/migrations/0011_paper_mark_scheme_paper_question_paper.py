# Generated by Django 4.1.3 on 2022-11-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0010_alter_subject_papers_alter_subject_sessions"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="mark_scheme",
            field=models.FileField(
                blank=True, null=True, upload_to="mark_schemes/"
            ),
        ),
        migrations.AddField(
            model_name="paper",
            name="question_paper",
            field=models.FileField(
                blank=True, null=True, upload_to="question_papers/"
            ),
        ),
    ]
