from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title= models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Note: {self.title}"
    
class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="images")
    title = models.CharField(max_length=200, blank=True, null=True)
    image_file = models.ImageField(upload_to='vault_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else f"Image {self.id} by {self.user.username}"
    
class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="documents")
    title = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='vault_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Doc: {self.title or 'Untitled'}"