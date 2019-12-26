from django.test import Client
from django.test import SimpleTestCase
import json

class ServicesTests(SimpleTestCase):

    def testHomePage(self):
        print ('\n+++ testHomePage +++')
        response = Client().get('')
        try:
            self.assertEquals(response.status_code, 200)
        except Exception as e:
            raise (e)
        else:
            msg = 'Ejecución correcta:\nResultado esperado: {}\nResultado recibido: HTTP {}'.format('HTTP 200', response.status_code)
            print(msg)

    def testResponse(self):
        print('\n+++ testResponse ++++')
        data = {}
        data['result'] = '18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1'
        jsonsample = json.dumps(data)
        response = Client().get('/seq/?initnum=18')
        try:
            self.assertJSONEqual(raw = response.content, expected_data = jsonsample, msg='El calculo de resultado es erroneo')
        except Exception as e:
            raise (e)
        else:
            msg = 'Ejecución correcta:\nResultado esperado: {}\nResultado recibido: {}'.format(jsonsample,response.content)
            print(msg)

    def testNumOnly(self):
        print('\n+++ testNumOnly ++++')
        response = Client().get('/seq/?initnum=a')
        data = {}
        data['error'] = 'Debe ingresar solo numeros'
        jsonsample = json.dumps(data)
        try:
            self.assertJSONEqual(raw = response.content, expected_data = jsonsample, msg=str(data['error']))
        except Exception as e:
            raise (e)
        else:
            msg = 'Ejecución correcta:\nResultado esperado: {}\nResultado recibido: {}'.format(jsonsample,response.content)
            print(msg)


    def testGreaterThanZero(self):
        print('\n+++ testGreaterThanZero ++++')
        response = Client().get('/seq/?initnum=-10')
        data = {}
        data['error'] = 'El numero debe ser mayor que 0'
        jsonsample = json.dumps(data)
        try:
            self.assertJSONEqual(raw = response.content, expected_data = jsonsample, msg=str(data['error']))
        except Exception as e:
            raise (e)
        else:
            msg = 'Ejecución correcta:\nResultado esperado: {}\nResultado recibido: {}'.format(jsonsample,response.content)
            print(msg)
