# Generated by Django 3.1.7 on 2021-03-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
