from django.conf import settings
from django.db import models
from django.urls import reverse

class station(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor")
    name = models.CharField('Nazwa', max_length=120)
    shortName = models.CharField('Skrót nazwy', max_length=20)
    slug = models.CharField('Slug', max_length=120)
    stationCreateDate = models.DateField('Data założenia')
    seismometerNumber = models.CharField('Nr sejsmometru', max_length=20)

    longitude = models.CharField('Długość geogr.', max_length=20)
    latitude = models.CharField('Szerokość geogr.', max_length=20)
    suchaX = models.IntegerField('Sucha Góra X', null=True, blank=True)
    suchaY = models.IntegerField('Sucha Góra Y', null=True, blank=True)
    height = models.IntegerField('Wysokość')

    moreInfo = models.TextField('Więcej informacji', null=True, blank=True)
    images = models.ImageField('Załączniki - zdjęcia', upload_to='uploads/stations/attachments', null=True, blank=True)
    files = models.FileField('Załączniki - pliki', upload_to='uploads/stations/attachments', null=True, blank=True)
    publishedDate = models.DateTimeField('Data publikacji')

    class Meta:
        verbose_name = "Stacja sejsmiczna"
        verbose_name_plural = "Stacje sejsmiczne"



    def __str__(self):
        return self.name + " (%s)" % self.shortName


    # def get_absolute_url(self):
    #     return reverse('localQuakes:detail', args=[str(self.id)])







