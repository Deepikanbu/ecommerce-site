# Generated by Django 4.2.4 on 2023-08-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_upload2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('fileimage', models.FileField(upload_to='djangoapp/static')),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]
