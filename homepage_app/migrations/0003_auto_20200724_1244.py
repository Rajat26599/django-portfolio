# Generated by Django 2.2.4 on 2020-07-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage_app', '0002_skills_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='icon',
            new_name='icon_file',
        ),
        migrations.AddField(
            model_name='skills',
            name='icon_url',
            field=models.URLField(null=True),
        ),
    ]