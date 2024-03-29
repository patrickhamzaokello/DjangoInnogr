from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(default = "Add Post Summary")
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited= models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    

class NewsArticle(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    newsdate = models.CharField(max_length=300)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content


class Preference(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
       
class Sensor(models.Model):
    sensorname = models.CharField(max_length=100)
    devicename = models.CharField(max_length=100)
    sensorvalue = models.CharField(max_length=100)
    date_recieved = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.sensorname
    
class Currentreading(models.Model):
    name = models.CharField(max_length=100)
    sensorval = models.CharField(max_length=100)
    date_recieved = models.DateTimeField(default=timezone.now)
    last_update= models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    