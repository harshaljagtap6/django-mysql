# Generated by Django 5.0.1 on 2024-01-18 05:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "myapiapp",
            "0002_employee_rename_employeeid_departments_departmentid_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="EmoployeeName",
            new_name="EmployeeName",
        ),
    ]
