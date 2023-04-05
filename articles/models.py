from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50,blank=False,null=False)  # 의미 파악 못함
    contents = models.TextField(blank=False,null=False)  # 이것도
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey("Article",related_name="post",on_delete=models.CASCADE,db_column="post_id")
    contents = models.TextField(blank=False,null=False)