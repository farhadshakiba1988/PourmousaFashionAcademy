# Generated by Django 4.2.5 on 2023-09-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='image'),
        ),
    ]