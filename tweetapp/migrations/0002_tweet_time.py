# Generated by Django 4.2.5 on 2023-09-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweetapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="time",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
