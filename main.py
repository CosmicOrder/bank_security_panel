import datetime
import os

import django
from django.utils.timezone import localtime, make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit, Passcard

if __name__ == '__main__':
    passcard = Passcard.objects.all()[0]
    visits = Visit.objects.filter(passcard=passcard)
    print(visits)
