from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
__all__ = ['Recruiter','CV','Angajat','Anunt']


class Recruiter(models.Model):
    user = models.OneToOneField(User, related_name="recruiter_profile",  on_delete=models.CASCADE)
    company = models.CharField(max_length=30)

class Anunt(models.Model):
    titlu = models.CharField(max_length=100)
    descriere = models.CharField(max_length=1000)
    created_by = models.ForeignKey(Recruiter, related_name="anunturi", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CV(models.Model):
    nume = models.CharField(max_length=40)
    anunturi = models.ManyToManyField(Anunt,related_name="aplicatii")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Angajat(models.Model):
    cvs = models.ForeignKey(CV, related_name="angajat", on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, related_name="angajat_profile",  on_delete=models.CASCADE)

