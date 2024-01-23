# Generated by Django 5.0.1 on 2024-01-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('created_by', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
