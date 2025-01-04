# Generated by Django 5.0.7 on 2024-11-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowescape', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smme_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cipc_reg', models.IntegerField()),
                ('operating_years', models.IntegerField()),
                ('sars_compliance', models.CharField(max_length=100)),
                ('cipc_docs', models.FileField(blank=True, null=True, upload_to='CIPC_docs/')),
                ('company_profiles', models.FileField(blank=True, null=True, upload_to='Company_profiles/')),
                ('bbbee_cert', models.FileField(blank=True, null=True, upload_to='BBBEE_certificates/')),
            ],
        ),
    ]
