from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=100)
    
    def __str__(self):
        return self.comment