# Generated by Django 4.0.3 on 2022-04-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('url1', models.URLField()),
                ('url2', models.URLField()),
                ('url3', models.URLField()),
                ('url4', models.URLField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
