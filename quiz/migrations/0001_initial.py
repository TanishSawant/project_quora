# Generated by Django 3.1.2 on 2020-10-18 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testId', models.TextField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='testScoreData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoreOfUser', models.BigIntegerField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField(unique=True)),
                ('optionA', models.TextField()),
                ('optionB', models.TextField()),
                ('optionC', models.TextField()),
                ('optionD', models.TextField()),
                ('CorrectOption', models.CharField(max_length=2)),
                ('questionId', models.TextField(unique=True)),
                ('subject', models.CharField(max_length=50)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.test')),
            ],
        ),
    ]
