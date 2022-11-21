# Generated by Django 3.2 on 2022-11-21 07:51

from django.db import migrations, models

import app.books.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='標題')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('cover_image', models.ImageField(null=True, upload_to=app.books.models.cover_directory_path, verbose_name='封面')),
            ],
            options={
                'verbose_name': '書本',
                'verbose_name_plural': '書本',
            },
        ),
    ]