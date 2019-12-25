from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json

def calc(request):
    result = ''
    data = {}
    data['result'] = ''
    try:
        num = int(request.GET.get('initnum'))
        if num > 0 :
            while num != 1:
                if num % 2 == 0:
                    result += str(int(num)) + ', '
                    num = num / 2
                else:
                    result += str(int(num)) + ', '
                    num = (num * 3) + 1
            if num == 1:
                result += '1'
            data['result'] = result
            json_data = json.dumps(data)
        else:
            result = 'El numero debe ser mayor que 0'
            data['result'] = result
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type='application/json',status = 400)

        return HttpResponse(json_data, content_type='application/json',status = 200)

    except Exception as e:
        result = 'Debe ingresar solo numeros'
        data['result'] = result
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json',status = 400)

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
