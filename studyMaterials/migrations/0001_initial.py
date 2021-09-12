# Generated by Django 3.2.6 on 2021-09-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.CharField(default='none', max_length=50)),
                ('date', models.CharField(default='none', max_length=50)),
                ('category', models.CharField(default='none', max_length=100)),
                ('description', models.CharField(default='none', max_length=100)),
                ('pdf', models.FileField(upload_to='media')),
            ],
        ),
    ]
