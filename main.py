import datetime
import os

import django
from django.utils.timezone import localtime, make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit, Passcard

if __name__ == '__main__':
    def get_duration(visit):
        if visit.leaved_at is None:
            return make_aware(datetime.datetime.now()) - visit.entered_at
        else:
            return visit.leaved_at - visit.entered_at

    def is_visit_long(visit, minutes=60):
        duration = get_duration(visit)
        duration_in_minutes_minutes = duration.total_seconds() // 60
        return True if duration_in_minutes_minutes >= minutes else False

    passcard = Passcard.objects.all()[0]
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        if is_visit_long(visit):
            print('Визиты дольше 60 минут: ', visit)
