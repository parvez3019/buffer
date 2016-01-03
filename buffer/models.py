from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now = False)

	def __unicode__(self):
		return self.email
