from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    OS_CHOICE = {
        ('hardware','하드웨어'),
        ('software','소프트웨어'),
        ('etc','기타')
    }
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_board')
    OS = models.CharField(max_length=80, choices=OS_CHOICE, null=True)
    title = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='board/%Y/%m/%d', default='board/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + "" + self.OS + "" + self.title + "" + self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('board:board_detail', args=[str(self.id)])
