import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit

if __name__ == '__main__':
    visitors = Visit.objects.all()
    print(visitors)


