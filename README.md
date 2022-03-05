# Movie Ticket Reservations
Algoritmo en la cual se simula cómo es que funciona la reservación de entradas para el cine. Fue desarrollado para el usuario del punto de vista de cliente.

El algoritmo fue diseñado para que el usuario pudiera:
- Ver las peliculas que se encuentran en cartelera y su información 
- Escoger una película en la cual se desee reservar entradas 
- Escoger la hora de la función más conveniente
- Definir la cantidad de asientos que desee y su localidad en la sala
- Realizar la reservación
- Confirmar que la reservación sea correcta

El lenguaje utilizado para el algoritmo fue python, en la cual se utiliza la librería de numpy para poder trabajar con arrays tanto unidimensionales como multidimensionales. Así mismo se implementan las clases con NamedTuple, representando los structs para la información de la reservación. También se levantó el API por medio de flask y jinja2 para poder trabajar con html.

- **Prueba Unitaria** pytest
- **Profiling** cProfile
- **Requests** Postman

### Cómo ejecutarlo?
1. Encontrar el file 'app.py' para poder correr el api.
```
cd MovieTicketReservations
```

2. Correr aplicación ejecutando el siguiente comando
```
python3 app.py
```

3. Interactuar con los distintos paths para reservar entradas al cine.

### Recursos
- html template: https://www.w3schools.com/w3css/w3css_templates.asp
- clases NamedTuple: https://realpython.com/python-namedtuple/
- flask: https://www.fullstackpython.com/flask.html
- numpy arrays: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
