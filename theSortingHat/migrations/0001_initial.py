# Generated by Django 2.2.2 on 2019-06-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('hat', models.CharField(choices=[('Griffindor', 'Griffindor'), ('Hufflepuff', 'Hufflepuff'), ('Ravenclaw', 'Ravenclaw'), ('Slitherin', 'Slitherin')], max_length=10)),
            ],
        ),
    ]
