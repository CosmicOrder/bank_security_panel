import datetime
import os

import django
from django.utils.timezone import localtime, make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit

if __name__ == '__main__':
    visitors = Visit.objects.filter(leaved_at=None)
    for visitor in visitors:
        entered_at = localtime(visitor.entered_at)
        now = make_aware(datetime.datetime.now())
        located_time = now - entered_at
        print(visitor.passcard)
        print('Зашёл в хранилище, время по Москве: ', entered_at)
        print('Находится в хранилище: ', located_time)
