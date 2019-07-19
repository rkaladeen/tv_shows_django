from django.db import models
# from time import strftime, strptime
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    
    if len(postData['title']) < 1:
      errors['title'] = "Show title is required"
    elif len(postData['title']) < 2:
      errors['title'] = "Show title should be at least 2 character" 
    if len(postData['network']) < 1:
      errors['network'] = "Show network is required"
    elif len(postData['network']) < 3:
      errors['network'] = "Show network should be at least 3 character"
    if len(postData['rdate']) < 1:
      errors['rdate'] = "Show Release Date is required"
    else:
      selected_date = datetime.strptime(postData['rdate'], "%Y-%m-%d")
      if selected_date > datetime.now():
        errors['rdate'] = "Please select a date in the past"
    if len(postData['desc']) > 0 and len(postData['desc']) < 10:
      errors['desc'] = "Show Description must have more than 10 characters"
    return errors

class Show(models.Model):
  # ID
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=45)
  release = models.DateField(null=True)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()