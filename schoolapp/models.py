from django.db import models

RESULT_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    )
# Create your models here.
class SeniorOne(models.Model):
    # Personal Information
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

    # Academic Results
    english = models.TextChoices('1', '2', '3', '4', '5', '6', '7', '8', '9')
    mathematics = models.TextChoices('1', '2', '3', '4', '5', '6', '7', '8', '9')
    social_studies = models.TextChoices('1', '2', '3', '4', '5', '6', '7', '8', '9')
    science = models.TextChoices('1', '2', '3', '4', '5', '6', '7', '8', '9')
    aggregates = models.Choices('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    division = models.Choices('1', '2', '3', '4')
    results_photo = models.ImageField(upload_to='results_photos')

    


