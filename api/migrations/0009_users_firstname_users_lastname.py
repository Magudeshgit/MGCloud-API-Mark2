# Generated by Django 4.1.3 on 2024-07-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_fileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
