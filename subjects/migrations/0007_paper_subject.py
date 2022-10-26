# Generated by Django 4.1.2 on 2022-10-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0006_remove_paper_subject_subject_papers"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="subject",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subject",
                to="subjects.subject",
            ),
            preserve_default=False,
        ),
    ]
