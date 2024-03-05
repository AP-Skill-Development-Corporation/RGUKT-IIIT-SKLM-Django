# Generated by Django 3.2 on 2024-03-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epid', models.CharField(max_length=15)),
                ('ename', models.CharField(max_length=50)),
                ('edesg', models.CharField(choices=[('0', '-- Select your Designation --'), ('1', 'Intern'), ('2', 'Junior Trainee'), ('3', 'Junior Developer'), ('4', 'Senior Trainee')], default='0', max_length=5)),
                ('esal', models.IntegerField(default=12000)),
            ],
        ),
    ]
