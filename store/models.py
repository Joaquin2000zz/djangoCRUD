from django.db import models as m
from uuid import uuid4

# Create your models here.

def generate_id():
    '''
    used for avoid:
    raise ValueError("Cannot serialize function: lambda")
    ValueError: Cannot serialize function: lambda
    '''
    return str(uuid4())

class Product(m.Model):
    '''table columns'''
    id = m.CharField(primary_key=True, max_length=len(str(uuid4())),
                     default=generate_id)
    name = m.CharField(max_length=64, null=False)
    price = m.IntegerField(null=False)

    def __str__(self):
        return '{}.{}'.format(self.id, self.name)
