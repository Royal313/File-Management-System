# Generated by Django 4.1.5 on 2023-03-04 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docs', '0003_document_delete_filesmodel_remove_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]