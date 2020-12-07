# Generated by Django 2.2.5 on 2020-10-09 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsp_project_app', '0013_auto_20201009_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Post_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nsp_project_app.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
