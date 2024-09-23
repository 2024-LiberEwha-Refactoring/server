# Generated by Django 5.1.1 on 2024-09-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booths', '0003_menus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='is_vegan',
            field=models.CharField(choices=[('PESCO', '페스코'), ('VEGAN', '비건')], max_length=10),
        ),
    ]
