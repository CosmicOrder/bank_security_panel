import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    passcard = passcards[99]

    print('owner_name:', passcard.owner_name)
    print('passcode:', passcard.passcode)
    print('created_at:', passcard.created_at)
    print('is_active:', passcard.is_active)
