from django.conf import settings
from django.db import models

class localQuake(models.Model):

    MAGNITUDE_SCALES = (
        ('ML', 'Magnituda lokalna (ML)'),
        ('Ms', 'Magnituda z fali powierzchniowej (Ms)'),
        ('Mb', 'Magnituda z fali poprzecznej (Mb)'),
        ('Mw', 'Magnituda z momentu sejsmicznego (Mw)'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor")
    eventDate = models.DateTimeField('Data i czas')
    magnitude = models.DecimalField('Magnituda', max_digits=3, decimal_places=1)
    magnitudeScale = models.CharField('Skala magnitudy', max_length=2, choices=MAGNITUDE_SCALES, default='ML')
    energy = models.BigIntegerField('Energia', null=True, blank=True)
    city = models.CharField('Miasto', max_length=60)
    region = models.CharField('Region/Kopalnia', max_length=200, null=True, blank=True)
    moreInfo = models.TextField('Więcej informacji', null=True, blank=True)

    longitude = models.CharField('Długość geogr.', max_length=20)
    latitude = models.CharField('Szerokość geogr.', max_length=20)
    suchaX = models.IntegerField('Sucha Góra X', null=True, blank=True)
    suchaY = models.IntegerField('Sucha Góra Y', null=True, blank=True)
    depth = models.IntegerField('Głębokość')
    depthPPM = models.IntegerField('Głębokość p.p.m.', null=True, blank=True)

    seismogram = models.FileField('Sejsmogram', upload_to='uploads/localQuakes/seismograms')
    attachments = models.FileField('Załączniki', upload_to='uploads/localQuakes/atachments', null=True, blank=True)
    publishedDate = models.DateTimeField('Data publikacji')

    class Meta:
        verbose_name = "Wstrząs lokalny"
        verbose_name_plural = "Wstrząsy lokalne"



    def __str__(self):
        return "Wstrząs o id: %d | " % (self.id) + "Data zdarzenia: {:%d  %b %Y}".format(self.eventDate)






