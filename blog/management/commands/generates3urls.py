from django.core.management.base import BaseCommand, CommandError
from blog.models import Article as articles
from blog.aws import upload_to_s3

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
       
        for article  in articles.objects.all():
            if not article._s3_image_path and article.article_image:
                try:
                   key = article.article_image.name.split('/')[-1]
                   url = upload_to_s3(article.article_image.read(), key)
                   article._s3_image_path = url
                   article.save()
                   self.stdout.write(self.style.SUCCESS(
                       'Successfully uploaded the  "%s" to s3 url is "%s"' % (article, article.article_image)))
                except:
                    raise CommandError('Exception occured')
                

            
