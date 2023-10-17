# Generated by Django 4.2.5 on 2023-09-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_slide_image_design_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='image_design',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_lebaseshab',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_nazokdozy',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_pourmousa',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_pourmousa_oje',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_pourmousa_savabegh',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_slide',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image_tanbour',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='course_image'),
        ),
    ]
