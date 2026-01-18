from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  

class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]

    title = models.CharField(max_length=256)
    content = models.TextField()

    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag)

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


