# Generated by Django 5.1.2 on 2024-11-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('select_service', models.CharField(choices=[('Service 1', 'One'), ('Service 2', 'Two'), ('Service 3', 'Three')], default='Service 1', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
