# Generated by Django 5.1.6 on 2025-02-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeniorOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('reg_no', models.CharField(max_length=10, unique=True, verbose_name='Registration Number')),
                ('emergency_contact', models.CharField(max_length=10, verbose_name='Emergency Contact')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Sex')),
                ('status', models.CharField(choices=[('Day', 'Day'), ('Boarding', 'Boarding')], max_length=10, verbose_name='Status')),
                ('cls', models.CharField(choices=[('Senior One', 'Senior One'), ('Senior Two', 'Senior Two'), ('Senior Three', 'Senior Three'), ('Senior Four', 'Senior Four')], max_length=20, verbose_name='Class')),
                ('elective', models.CharField(choices=[('ICT', 'ICT'), ('Music', 'Music'), ('French', 'French'), ('CRE', 'CRE'), ('Literature', 'Literature'), ('Agriculture', 'Agriculture'), ('Technical Drawing', 'Technical Drawing'), ('Food and Nutrition', 'Food and Nutrition'), ('Art and Design', 'Art and Design')], max_length=20, verbose_name='Elective Subject')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('date_of_admission', models.DateField(auto_now_add=True, verbose_name='Date of Admission')),
                ('religion', models.CharField(choices=[('Catholic', 'Catholic'), ('Christian', 'Christian'), ('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Adventist', 'Adventist'), ('Other', 'Other')], max_length=20, verbose_name='Religion')),
                ('former_school', models.CharField(max_length=100, verbose_name='Former School')),
                ('index_no', models.CharField(max_length=10, verbose_name='Index Number')),
                ('hobbies', models.CharField(max_length=100, verbose_name='Hobbies')),
                ('dream_profession', models.CharField(choices=[('Doctor', 'Doctor'), ('Engineer', 'Engineer'), ('Lawyer', 'Lawyer'), ('Pilot', 'Pilot'), ('Teacher', 'Teacher'), ('Nurse', 'Nurse'), ('Accountant', 'Accountant'), ('Journalist', 'Journalist'), ('Artist', 'Artist'), ('Musician', 'Musician'), ('Farmer', 'Farmer'), ('Other', 'Other')], max_length=20, verbose_name='Dream Profession')),
                ('nationality', models.CharField(max_length=100, verbose_name='Nationality')),
                ('student_nin', models.CharField(max_length=100, verbose_name='Student NIN')),
                ('student_lin', models.CharField(max_length=100, verbose_name='Student LIN')),
                ('home_address', models.CharField(max_length=100, verbose_name='Home Address')),
                ('district', models.CharField(max_length=100, verbose_name='District')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('special_needs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Special Needs')),
                ('medical_history', models.TextField(max_length=100, verbose_name='Medical History')),
                ('english', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, verbose_name='English')),
                ('mathematics', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, verbose_name='Mathematics')),
                ('social_studies', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, verbose_name='Social Studies')),
                ('science', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, verbose_name='Science')),
                ('aggregates', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, verbose_name='Aggregates')),
                ('division', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, verbose_name='Division')),
                ('results_photo', models.ImageField(upload_to='results_photos', verbose_name='Results Photo')),
            ],
        ),
    ]
