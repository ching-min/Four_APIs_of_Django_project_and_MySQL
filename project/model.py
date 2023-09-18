from django.db import models
# Create your models here.
class Articles(models.Model):
    date = models.DateField(primary_key=True) #models.DateTimeField(auto_now_add=False)
    #author = models.TextField()
    title = models.TextField()
    #href = models.TextField()
    #pushcount = models.TextField()
    content = models.TextField()
    tags = models.TextField()
	
    class Meta:
        db_table = 'articles'