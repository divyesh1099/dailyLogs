from django.db import models
from django.conf import settings

# Create your models here.
class LogEntry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logOfUser')
    updated_at = models.DateTimeField(auto_now=True)

    # Sentiment
    mood = models.CharField(max_length=50, blank=True)

    # Text Analysis
    keywords = models.TextField(blank=True)
    summary = models.TextField(blank=True)

    # User Interaction
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "LogEntries"

    def __str__(self):
        return self.title