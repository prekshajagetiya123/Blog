from django.conf import settings
from django.db import models
from restaurants.models import RestaurantLocation
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    #associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.DO_NOTHING)

    #item stuff
    name          = models.CharField(max_length = 200)
    contents      = models.TextField(help_text = 'Separate each iten by comma')
    excludes      = models.TextField(blank = True, null = True, help_text = 'Separate each iten by comma')
    public        = models.BooleanField(default = True)
    timestamp     = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs ={'pk': self.pk})

    # return f"/restaurants/{self.slug}"

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
