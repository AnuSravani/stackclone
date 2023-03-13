from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


# Create your models here.
class Questions(models.Model):
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_date"]
    def __str__(self):
        return self.description
    # answer list cheyyunna line
    @property
    def question_answers(self):
        return Answers.objects.filter(question=self).annotate(ucount=Count('upvote')).order_by('-ucount')
    

class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    answer=models.CharField(max_length=500)
    upvote=models.ManyToManyField(User,related_name="answer")

    @property
    def upvote_count(self):
        return self.upvote.all().count()
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profiles",null=True)
    bio=models.CharField(max_length=200)

    @property
    def question_count(self):
        return Questions.objects.filter(User=self.user).count()
