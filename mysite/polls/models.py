from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date of publish')

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)