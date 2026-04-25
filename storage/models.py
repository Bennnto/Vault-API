from django.db import models
from django.contrib.auth.models import User



class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)
    

class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    function = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="pictures/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.label} i- {self.created_date}"

