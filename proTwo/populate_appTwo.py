import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        #create the fake data for that entry
        fake_name = fakegen.name().split()
        fake_firstName = fake_name[0]
        fake_lastName = fake_name[1]
        fake_email = fakegen.email()

        #create new entry
        user = User.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script !")
    populate(20)
    print("Populating complete")