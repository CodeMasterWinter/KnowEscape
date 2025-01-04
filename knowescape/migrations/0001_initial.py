# Generated by Django 5.0.7 on 2024-10-31 14:48

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('home_address', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='ZA')),
                ('disability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('disability_note', models.FileField(blank=True, null=True, upload_to='disability_notes/')),
                ('certified_id', models.FileField(upload_to='certified_ids/')),
                ('matric_certificate', models.FileField(blank=True, null=True, upload_to='matric_certificates/')),
            ],
        ),
    ]
