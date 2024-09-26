from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=228)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=228)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images/")
    tags = models.ManyToManyField(Tag, null=True)
    views = models.PositiveBigIntegerField()
    created_data = models.DateField(auto_now_add=True)

    def __strs__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    author_full_name = models.CharField(max_length=228)
    author_image = models.ImageField(upload_to="author_image/",null=True, blank=True)
    comment = models.TextField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author_full_name

