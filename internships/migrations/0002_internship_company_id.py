# Generated by Django 5.2 on 2025-05-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='company_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
