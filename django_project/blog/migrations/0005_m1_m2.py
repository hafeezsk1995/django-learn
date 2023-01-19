# Generated by Django 4.0.5 on 2022-06-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_mymodel_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='M1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=80)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]