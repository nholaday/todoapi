# Generated by Django 4.0.1 on 2022-01-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
