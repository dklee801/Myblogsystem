from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField('작성자',max_length=20)
    contents = models.TextField('글내용', max_length= 1000) #TextField: 여러 줄 입력 양식

    def __str__(self):
        return self.contents
