from django.db import models

# Create your models here.

# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# class Role(models.Model):
# role_name = models.CharField(max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True)
    location = models.CharField(max_length=50)
    bio = models.TextField(max_length=50)
    registration_date = models.DateField(auto_now=False, auto_now_add=False)
    picture = models.ImageField(height_field=None, width_field=None, max_length=2000)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    budget = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    created_date = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)


class SkillCategory(models.Model):
    category_name = models.CharField(max_length=50)


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    date_earned = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FreelancerSkill(models.Model):
    created_date = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FreelancerPayment(models.Model):
    amount = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    payment_to = models.ForeignKey(User, on_delete=models.CASCADE)


class ClientPayment(models.Model):
    amount = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
#     payment_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class LoggingInfo(models.Model):
    activity = models.TextField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class JobProposal(models.Model):
    freelancer_comment = models.TextField(max_length=255)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)


class Attachment(models.Model):
    files = models.CharField(max_length=255)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)


class JobSkill(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
