# Generated by Django 4.2.6 on 2023-10-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120)),
                ('bug_type', models.CharField(choices=[('error', 'Error'), ('feature', 'New Feature'), ('other', 'Other')], default='error', max_length=70)),
                ('report_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], default='to_do', max_length=20)),
            ],
        ),
    ]
