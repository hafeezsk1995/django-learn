# Generated by Django 4.0.6 on 2022-07-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='no', to='blog.customer'),
        ),
    ]