# Generated by Django 2.2.13 on 2021-03-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sysInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=50)),
                ('compiler', models.CharField(max_length=30)),
                ('cpu_architecture', models.CharField(max_length=20)),
            ],
        ),
    ]
