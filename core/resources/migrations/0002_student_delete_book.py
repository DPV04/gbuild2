# Generated by Django 5.0.3 on 2024-04-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.TextField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]