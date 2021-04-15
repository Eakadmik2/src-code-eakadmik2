# Generated by Django 3.2 on 2021-04-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staffs'), (3, 'Student')], default=1, max_length=10),
        ),
    ]
