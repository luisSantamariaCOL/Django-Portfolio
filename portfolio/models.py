from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)  # title of the project
    description = models.CharField(max_length=250)  # description of the project
    image = models.ImageField(upload_to="portfolio/images/")  # image of the project
    url = models.URLField(blank=True)  # url of the project

    def __str__(self):
        return self.title

