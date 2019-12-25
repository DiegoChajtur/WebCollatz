from django.test import TestCase
from django.test import Client
import json
class ViewTest(TestCase):

    def testCalc(self):
        response = Client().get('/seq/?initnum=10')
        if (response.status_code == 200):
            print ('Test OK')
