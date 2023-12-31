# Generated by Django 4.2.5 on 2023-09-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('img', models.ImageField(upload_to='image')),
                ('des', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_slide', models.ImageField(upload_to='media')),
                ('image_nazokdozy', models.ImageField(upload_to='media')),
                ('image_lebaseshab', models.ImageField(upload_to='media')),
                ('image_design', models.ImageField(upload_to='media')),
                ('image_tanbour', models.ImageField(upload_to='media')),
                ('image_pourmousa', models.ImageField(upload_to='media')),
                ('image_pourmousa_oje', models.ImageField(upload_to='media')),
                ('image_pourmousa_savabegh', models.ImageField(upload_to='media')),
            ],
        ),
    ]
