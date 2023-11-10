from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime



class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Article(models.Model):
    STATUS_OF_ARTICLE = (
        ("checking", "Checking"),
        ("rejected", "Rejected"),
        ("published", "Published"),
    )
    
    
    title = models.CharField(max_length=200)
    content= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=12, choices=STATUS_OF_ARTICLE, default="checking")
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d", null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+'-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)
            self.save()
            
    class Meta:
        ordering = ("-created",)
    
    def __str__(self) -> str:
        return f"{self.title} writed by {self.author}"
    
    def get_absolute_url(self):
        return reverse("blogs:blog_detail", kwargs={"slug": self.slug})
    
    
    objects = models.Manager()
    publish = PublishedManager()
    