# Secuencia de Collatz

Web-Service que devuelve en formato JSON,  la secuencia de Collatz según un número inicial

# Instalación

```bash
$ pip3 install django
```

# Ejecución

```bash
$ python3 manage.py runserver
```

# Instrucciones

Para que devuelva la secuencia es necesario enviar una petición ```GET ``` con el parámetro ```initnum ``` para entregarle número inicial que permitirá hacer el cálculo de la secuencia

```bash
curl -X GET 'http://127.0.0.1:8000/seq/?initnum=11'
```

y devolverá la secuencia en formato JSON

```json
{"result": "11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1"}
```
