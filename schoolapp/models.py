from django.db import models

# Create your models here.
class SeniorOne(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.IntegerField()
    last_name = models.CharField(max_length=100)

    reg_no = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10)
    sex = models.Choices('M', 'F')
    status = models.Choices('Day', 'boarding')

    cls = models.Choices('Senior One', 'Senior Two', 'Senior Three', 'Senior Four')
    elective = models.Choices('ICT', 'Music', 'French', 'CRE', 'Literature', 'Agriculture',  'Technical Drawing', 'Food and Nutrition', 'Art and Design', 'Literature',)
    date_of_birth = models.DateField()
    date_of_admission = models.DateField(auto_now_add=True)
    religion = models.Choices('Catholic','Christian', 'Muslim', 'Hindu', 'Adventist', 'Other')

    former_school = models.CharField(max_length=100)
    index_no = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=100)
    dream_profession = models.Choices('Doctor', 'Engineer', 'Lawyer', 'Pilot', 'Teacher', 'Nurse', 'Accountant', 'Journalist', 'Artist', 'Musician', 'Farmer', 'Other')
    nationality = models.CharField(max_length=100)
    student_nin = models.CharField(max_length=100)
    student_lin = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    district = models.CharField(max_length=100) 
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    special_needs = models.Choices('Yes', 'No')
    medical_History = models.TextField(max_length=100)


    