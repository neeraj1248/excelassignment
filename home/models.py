from django.db import models
from datetime import date

# Create your models here.
class Excl(models.Model):
    instructionid  = models.CharField(max_length = 20, blank = True)
    case_ref_no  = models.CharField(max_length = 50, blank = True)
    client_name  = models.CharField(max_length = 50, blank = True)
    candidate_name  = models.CharField(max_length = 50, blank = True)
    address  = models.CharField(max_length = 300, blank = True)
    stay_period= models.CharField(max_length = 20, blank = True)
