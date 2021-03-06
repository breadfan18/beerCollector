# Generated by Django 3.2.4 on 2021-07-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_drinking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='drinking',
            name='date',
            field=models.DateField(verbose_name='drinking date'),
        ),
    ]
