from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
  title = models.CharField(default="", max_length=255)
  text = models.TextField(default="")
  added_ad = models.DateTimeField(null=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, related_name="question_author")
  likes = models.ManyToManyField(
        User, related_name="question_like", blank=True)

  class Meta:
        ordering = ('-added_at',)

  def __str__(self):
        return self.title

  def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})



class Answer(models.Model):
  text = models.TextField(default="")
  added_ad = models.DateTimeField(null=True)
  question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  
  def __str__(self):
        return self.text
