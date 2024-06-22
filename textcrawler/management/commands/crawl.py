import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from textcrawler.models import CrawlLog
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Crawl Django documentation'

    def handle(self, *args, **kwargs):
        start_time = timezone.now()
        log = CrawlLog(start_time=start_time, status='Running')
        log.save()

        url = 'https://docs.djangoproject.com/en/stable/'
        response = requests.get(url)

        if response.status_code != 200:
            log.status = 'Failed'
            log.error_message = f'Failed to retrieve content. Status code: {response.status_code}'
            log.end_time = timezone.now()
            log.save()
            self.stderr.write(self.style.ERROR('Failed to retrieve content.'))
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = soup.get_text()

        try:
            with open('django_docs.txt', 'w', encoding='utf-8') as f:
                f.write(text_content)
        except Exception as e:
            log.status = 'Failed'
            log.error_message = str(e)
            log.end_time = timezone.now()
            log.save()
            self.stderr.write(self.style.ERROR('Saving to file failed'))
            return

        log.status = 'Completed'
        log.end_time = timezone.now()
        log.save()
        self.stdout.write(self.style.SUCCESS('Crawling completed successfully'))
