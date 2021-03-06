# Secuencia de Collatz

Web-Service que devuelve en formato JSON, la secuencia de Collatz según un número inicial.

# Instalación

```bash
$ pip3 install django
```

# Ejecución

```bash
$ python3 manage.py runserver
```

# Instrucciones

Para que devuelva la secuencia es necesario enviar una petición ```GET``` con el parámetro ```initnum``` a la dirección ```http://127.0.0.1:8000/seq/``` para entregarle número inicial que permitirá hacer el cálculo de la secuencia.

Puedes utilizar cURL, Postman, o cualquier cliente ```HTTP```.

Ejemplo en cURL:
```bash
curl -X GET 'http://127.0.0.1:8000/seq/?initnum=11'
```
Respuesta:
```json
{"result": "11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1"}
```

# Pruebas de funcionamiento

El siguiente script ejecuta todas las pruebas y genera un reporte 

```bash
$ ./testAll.sh
```

Las pruebas que se realizan son las siguientes:

- testHomePage: Realiza una petición esperando como resultado código 200
- testResponse: Realiza una prueba en el cálculo de la secuencia, comparando un resultado precalculado con la respuesta del servidor
- testNumOnly: Realiza una prueba si es que se ingresa algún caractér diferente a un número
- testGreaterThanZero: Realiza una verificación si es que el numero ingresado es mayor a 0