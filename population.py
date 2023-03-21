import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bestbarber.settings')

import django

django.setup()
from barbers.models import BarberShop, User


def populate():
    barbers_barbershop = [
        {
            'id': 1,
            'name': 'shop1',
            'location': 'location1',
            'description': 'barber1_description',
            'service': 'barber1_service',
            'type': 'type1',
            'style': 'style1',
            'price': 10},
        {
            'id': 2,
            'name': 'shop2',
            'location': 'location2',
            'description': 'barber2_description',
            'service': 'barber2_service',
            'type': 'type2',
            'style': 'style2',
            'price': 20},

    ]

    barbers_barbershop2 = [
        {'id':3,
        'name': 'shop3',
         'location': 'location3',
         'description': 'barber3_description',
         'service': 'barber3_service',
         'type': 'type3',
         'style': 'style3',
         'price': 30},
        {'id':4,
        'name': 'shop4',
         'location': 'location4',
         'description': 'barber4_description',
         'service': 'barber4_service',
         'type': 'type4',
         'style': 'style4',
         'price': 40},

    ]

    barbers_managerprofile = {'manager1': {'password': '11111', 'shop': barbers_barbershop},
                              'manager2': {'password': '11111', 'shop': barbers_barbershop2}}

    def add_user(name, password):
        user = User.objects.get_or_create(username=name)[0]
        user.set_password(password)
        user.save()
        return user

    def add_shop(user,id, name, location, description, service, type, style, price):
        c = BarberShop.objects.get(manage_by=user,id = id)
        c.name = name
        c.location = location
        c.description = description
        c.service = service
        c.type = type
        c.style = style
        c.price = price
        c.save()
        return c

    for manager, manager_data in barbers_managerprofile.items():
        user = add_user(manager, manager_data["password"])
        for p in manager_data['shop']:
            print(p)
            add_shop(user,
                     p['id'],
                     p['name'],
                     p['location'],
                     p['description'],
                     p['service'],
                     p['type'],
                     p['style'],
                     p['price'])


# Start execution here!
if __name__ == '__main__':
    print('Starting population script...')

populate()
