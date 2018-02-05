import web
from random import randint
random_page_generator = ['http://www.facebook.com',
                         'http://www.yahoo.com','http://www.google.com']
y=random_page_generator[randint(0,2)]
web.open(y, new=2)


