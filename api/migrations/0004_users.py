# Generated by Django 4.1.3 on 2024-06-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_fileupload_foreign_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MGRID', models.IntegerField(verbose_name='MGRealm ID')),
                ('username', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('app_session', models.CharField(max_length=50)),
                ('expiration', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'MGCloud Users',
            },
        ),
    ]