from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Post(models.Model):
    # CHOICES= (
    #     ('p', 'Published'),
    #     ('d', 'Draft'),
    # )
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    # category = models.ForeignKey(Category, related_name="category", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.PROTECT)
    # status = models.CharField(max_length=2, choices=CHOICES, default="d")
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

