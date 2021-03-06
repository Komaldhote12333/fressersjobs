# Generated by Django 4.0.1 on 2022-06-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=435)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=435)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=435)),
            ],
        ),
        migrations.CreateModel(
            name='Joblist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=235)),
                ('link', models.CharField(max_length=235)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.language')),
                ('locati', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.location')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.qualification')),
            ],
        ),
    ]
