from django.db import models

# A model that will log the status of the crawling process
class CrawlLog(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20)
    error_message = models.TextField(null=True, blank=True)

# added a str representation so that when read from the admin dashboard the data will be human friendly
    def __str__(self):
        return (
            f"Crawl start time: {self.start_time} - Status: {self.status} "
            f"Crawl end time: {self.end_time}"
        )

