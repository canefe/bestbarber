import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bestbarber.settings')

import django

django.setup()
from barbers.models import BarberShop, User,Comment
from barbers.views import resetBarber


def populate():
    barbers_barbershop = [
        {
            'name': 'shop1',
            'location': 'location1',
            'description': 'barber1_description',
            'service': 'barber1_service',
            'rating': 3,
            'type': 'type1',
            'style': 'style1',
            'price': 10},
        {
            'name': 'shop2',
            'location': 'location2',
            'description': 'barber2_description',
            'service': 'barber2_service',
            'rating': 3,
            'type': 'type2',
            'style': 'style2',
            'price': 20},
    ]

    barbers_barbershop2 = [
        {'name': 'shop3',
         'location': 'location3',
         'description': 'barber3_description',
         'service': 'barber3_service',
         'rating': 3,
         'type': 'type3',
         'style': 'style3',
         'price': 30},
    ]



    comments = [
        {
            'comment_text': "good shop",
            "rating":4,
            "attr":"Clean,Cheap"
        },
        {
            'comment_text': "Okay",
            "rating": 2,
            "attr": "Boring, Cheap"
        }

    ]
    comments2 = [
        {
            'comment_text': "impressive shop",
            "rating":5,
            "attr":"Clean,Professional"
        },
        {
            'comment_text': "good for student",
            "rating": 4,
            "attr": "Student,Cheap"
        }

    ]
    empty = [

    ]

    user_profile  = {'user1': {'password': '11111', 'shop': barbers_barbershop,'comment':comments},
                     'user2': {'password': '11111', 'shop': barbers_barbershop2,'comment':comments2}
    }

    def add_user(name, password):
        user = User.objects.get_or_create(username=name)[0]
        user.set_password(password)
        user.save()
        return user

    def add_shop(user, name, location, description, service, rating, type, style, price):
        shop = BarberShop.objects.get_or_create(manage_by=user, name=name)[0]
        shop.name = name
        shop.location = location
        shop.description = description
        shop.service = service
        shop.user_rating = rating
        shop.type = type
        shop.style = style
        shop.price = price
        shop.save()
        return shop

    def add_comment(user,shop,text,rating,attributes):
        comment = Comment.objects.get_or_create(user=user, barber_shop=shop)[0]
        comment.comment_text = text
        comment.rating = rating
        comment.attr = attributes
        comment.save()
        resetBarber()
        return shop

    for manager, manager_data in user_profile.items():
        user = add_user(manager, manager_data["password"])
        for p in manager_data['shop']:
            print(p)
            shop = add_shop(user,
                     p['name'],
                     p['location'],
                     p['description'],
                     p['service'],
                     p['rating'],
                     p['type'],
                     p['style'],
                     p['price'])
            for c in manager_data['comment']:
                add_comment(user,shop,c['comment_text'],c['rating'],c['attr'])


# Start execution here!
if __name__ == '__main__':
    print('Starting population script...')

populate()
