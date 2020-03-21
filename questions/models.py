from django.db import models
from questions.question_formatter import formatter
import string
from datetime import datetime
from nltk.stem import PorterStemmer

translator = str.maketrans('', '', string.punctuation)
ps = PorterStemmer() 

# Create your models here.

class Answer(models.Model):
    answer = models.TextField(default="")
    date_appended = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.CharField(max_length=150)
    question_searchable_string = models.CharField(default ="", max_length=200, blank=True)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    interrogative = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        searchable = sorted(str(self.question).lower().translate(translator).split())
        for s in searchable:
            if s in ['who','where','when','why','how','what','can']:
                self.interrogative = s
        
        self.question_searchable_string = formatter(self.question)
        super().save(*args, **kwargs)


