import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    active_passcards = []
    passcards = Passcard.objects.all()
    for passcard in passcards:
        if passcard.is_active:
            active_passcards.append(passcard)
    print(len(active_passcards))
