from django.db import models
# Create your models here.
class Articles(models.Model):
    date = models.DateField(primary_key=True) #models.DateTimeField(auto_now_add=False)
    title = models.TextField()
    content = models.TextField()
    tags = models.TextField()
	
    class Meta:
        db_table = 'articles'