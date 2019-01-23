import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

import random
from firstapp.models import Topic, AccessRecord, WebPage, CreditCard

from faker import Faker
fakegen = Faker()

topic = ['SEARCH_ENGINE','SOCIAL','GAMING','NEWS','MARKETPLACE']

def add_topic():
    t=Topic.objects.get_or_create(top_name = random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_cc = fakegen.credit_card_provider(card_type = None)

        webpg = WebPage.objects.get_or_create(topics = top, url = fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)

        credit_card = CreditCard.objects.get_or_create(name = webpg, card = fake_cc)

if __name__ == '__main__':
    print "Hello I am population the script"
    populate(20)
    print "Population is done successfully"
