# Generated by Django 4.1.2 on 2022-10-26 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0007_paper_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subject",
            name="papers",
        ),
    ]
