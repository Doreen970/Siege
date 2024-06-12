from django.db import models

# A model that will log the status of the crawling processs
class CrawlLog(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20)
    error_message = models.TextField(null=True, blank=True)
