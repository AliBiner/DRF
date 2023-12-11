from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    slug = models.SlugField(editable=False, unique=True, max_length=200)
    image = models.ImageField(upload_to='media/Post',null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Modified_by')

    def __str__(self):
        return self.title
    def get_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique_slug = slug
        number = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, number)
            number +=1

        return unique_slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.created= timezone.now()

        self.modified= timezone.now()
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)


