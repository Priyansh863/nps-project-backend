# Generated by Django 2.2.5 on 2020-10-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsp_project_app', '0002_auto_20200921_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Post_Title',
        ),
        migrations.AddField(
            model_name='content',
            name='Post_Title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]