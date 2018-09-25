from django.conf import settings
from django.db import models
from django.urls import reverse

class GlobalQuake(models.Model):

    MAGNITUDE_SCALES = (
        ('ML', 'Magnituda lokalna (ML)'),
        ('Ms', 'Magnituda z fali powierzchniowej (Ms)'),
        ('Mb', 'Magnituda z fali poprzecznej (Mb)'),
        ('Mw', 'Magnituda z momentu sejsmicznego (Mw)'),
    )

    TIME_ZONES = (
        ('UTC', 'Coordinated Universal Time (UTC)'),
        ('CET', 'Central European Time (UTC+1)'),
        ('CEST', 'Central European Time (UTC+2)'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor")
    eventDate = models.DateTimeField('Data i czas')
    timeZone = models.CharField('Strefa czasowa', max_length=4, choices=TIME_ZONES, default='UTC')
    magnitude = models.DecimalField('Magnituda', max_digits=3, decimal_places=1)
    magnitudeScale = models.CharField('Skala magnitudy', max_length=2, choices=MAGNITUDE_SCALES, default='Mw')
    region = models.CharField('Region/Kraj', max_length=200)
    moreInfo = models.TextField('Więcej informacji', null=True, blank=True)

    longitude = models.CharField('Długość geogr.', max_length=20)
    latitude = models.CharField('Szerokość geogr.', max_length=20)
    depth = models.IntegerField('Głębokość')

    seismogram = models.FileField('Sejsmogram', upload_to='uploads/globalQuakes/seismograms')
    attachments = models.FileField('Załączniki', upload_to='uploads/globalQuakes/atachments', null=True, blank=True)
    publishedDate = models.DateTimeField('Data publikacji')

    class Meta:
        verbose_name = "Trzęsienie ziemi"
        verbose_name_plural = "Trzęsienia ziemi"



    def __str__(self):
        return "Trzęsienie ziemi o id: %d | " % (self.id) + "Data zdarzenia: {:%d  %b %Y}".format(self.eventDate)


    def get_absolute_url(self):
        return reverse('globalQuakes:detail', args=[str(self.id)])







