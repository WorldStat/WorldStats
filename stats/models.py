from django.db import models

class Article(models.Model):

    Health ='Health'
    Geography = 'Geography'
    Economy = 'Economy'
    Other = 'Other'

    stat_cat = (
        (Health, 'Health'),
        (Geography, 'Geography'),
        (Economy, 'Economy'),
        (Other, 'Other')
    )

    title = models.CharField(max_length=130)
    about = models.TextField(max_length=340)
    content = models.TextField(max_length=1024)
    picture = models.FileField(upload_to='pictures/')
    publish = models.DateTimeField()
    source = models.URLField()
    category = models.CharField(max_length=32, choices=stat_cat, default=Other)

    def __str__(self) -> str:
        return str(self.title)
