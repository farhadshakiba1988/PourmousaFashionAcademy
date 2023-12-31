# Generated by Django 4.2.5 on 2023-09-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_slide_image_design_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
