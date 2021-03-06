# Generated by Django 2.2 on 2019-04-29 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('studied_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('second_review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('third_review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fourth_review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fifth_review_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
