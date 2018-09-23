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



@register.filter(name='absolutValue')
def absolutValue(value):

    return abs(float(value))