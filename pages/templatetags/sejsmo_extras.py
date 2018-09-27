from django import template
from decimal import *

register = template.Library()

@register.filter(name='quakeEnergy')
def quakeEnergy(value):

    # FLoat(value)
    # Decimal(value)

    upper = Decimal(1.8)+(Decimal(1.9)*value)
    result = 10**upper

    if(value > 3):
        return round(result, -6)
    else:
        return round(result, -5)



@register.filter(name='correctLat')
def correctLat(lattitude):

    lattitude = float(lattitude)

    if lattitude > 0:
        return 'N'
    else:
        return 'S'

@register.filter(name='correctLong')
def correctLong(longitude):

    longitude = float(longitude)

    if longitude > 0:
        return 'E'
    else:
        return 'W'


@register.filter(name='absolutValue')
def absolutValue(value):

    return abs(float(value))