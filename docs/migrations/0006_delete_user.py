# Generated by Django 4.1.5 on 2023-03-04 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_alter_document_date_posted'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
