# Generated by Django 4.2.5 on 2023-09-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_slide_image_alter_slide_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='image',
        ),
        migrations.AddField(
            model_name='slide',
            name='image_design',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_lebaseshab',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_nazokdozy',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_pourmousa',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_pourmousa_oje',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_pourmousa_savabegh',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_slide',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AddField(
            model_name='slide',
            name='image_tanbour',
            field=models.ImageField(blank=True, null=True, upload_to='base/img'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
