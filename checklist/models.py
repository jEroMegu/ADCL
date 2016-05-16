from django.db import models

# Create your models here.
class User(models.Model):
	def __str__(self):
		return self.user_name
	user_name = models.CharField(max_length=20)

class Checklist(models.Model):
	def __str__(self):
		return self.item_name
	item_name = models.CharField(max_length=200)

class Result(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Checklist, on_delete=models.CASCADE)
	result = models.IntegerField(default=0)
