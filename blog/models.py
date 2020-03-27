from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(user__username__icontains=query)
                    )

        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    topic = models.CharField(max_length=40, default='Tech')
    title = models.CharField(max_length=120)
    imp = models.CharField(max_length=40, default='ok')
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=40, default='Technology')
    tag2 = models.CharField(max_length=40, default='Technology')
    tag3 = models.CharField(max_length=40, default='Technology')
    content = models.TextField(null=True, blank=True)
    after_imp = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time = models.CharField(max_length=10, default='2 min')
    html_keywords = models.TextField(null=True, blank=True)
    html_disc = models.TextField(null=True, blank=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
