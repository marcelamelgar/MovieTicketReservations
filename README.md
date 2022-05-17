# Movie Ticket Reservations
Algoritmo en la cual se simula cómo es que funciona la reservación de entradas para el cine. Fue desarrollado para el usuario del punto de vista de cliente. Como segunda parte del proyecto, se agregó que a cada reservación que se lleve a cabo, se le asigne un número de orden para que después alguien de la administración pueda buscar la orden y hasta cancelarla. También se le agregó el feature en que el cliente puede ir viendo cuáles son las próximas películas que se podrán ver en el cine. Incluso, se le añadió una sección de dulcería en dónde el puede ver el menú de comida y los combos de comida que hay.
Como entrega final, se realizaron unos cambios a las estructuras y algoritmos utilizados anteriormente para comparar la variación de performance entre cada feature. Estos cambios fueron enfocados a la manera en la que ahora se administran las películas, horas y salas para que el cliente pueda reservar sus entradas de cine. Se cambió el binary search tree con enfoque a búsqueda por algoritmos de ordenamiento y búsqueda, aunque este se quedara intacto al momento de eliminar una órden. Finalmente se agregó la opción de poder verificar en qué sala se lleva a cabo cierta función y qué funciones están asignadas a cierta sala. Como un plus para el algoritmo de grafo, se implementó Networkx para que así se pudiera visualizar la manera en la que están conectados los nodos del grafo.

El algoritmo fue diseñado para que el usuario pudiera:
- Ver las peliculas que se encuentran en cartelera y su información 
- Escoger una película en la cual se desee reservar entradas 
- Escoger la hora de la función más conveniente
- Definir la cantidad de asientos que desee y su localidad en la sala
- Realizar la reservación
- Confirmar que la reservación sea correcta
- Contar con un número de órden único
- Poder ver cuáles son las películas que estarán proximamente en el cine
- Ver el menú de comida del cine y los combos que ofrece
- Cancelar su reservación por medio de la busqueda de un administrador del cine
- Verificar en qué sala se lleva a cabo una función
- Verificar qué funciones fueron asignadas a una sala

El lenguaje utilizado para el algoritmo fue python, en la cual se utiliza la librería de numpy para poder trabajar con arrays tanto unidimensionales como multidimensionales. Así mismo se implementan las clases con NamedTuple, representando los structs para la información de la reservación. También se levantó el API por medio de flask y jinja2 para poder trabajar con html. Cuenta con las estructuras de Queue, Stack y trees, generados con clases y objetos. Así como también se le agregó un grafo dirigido, merge sort y jump search.

**Arrays Unidimensionales**: salas según las horas, asientos seleccionados por el cliente.

**Arrays Multidimensionales**: mapa de asientos, mapa de selección de asientos, horas según cada película.

**Structs**: clase en la que se tienen los datos de la reservación confirmada.

**Queue**: lista en la que se presentan las próximas películas que se presentan en órden

**Stack**: listas en las que se presentan las diferentes opciones de snacks y combos que ofrece el cine

**Tree**: Binary Search Tree en la que el administrador puede buscar un número único de orden y puede borrar/cancelar la orden.

**Grafo**: Grafo en la que se vinculas las peliculas, horas y salas. Permite la verificacion de sala y funciones.

**Merge Sort**: Algoritmo en la que se ordenan los numeros de orden para poder aplicar el Jump Search.

**Jump Search**: Algoritmo en la que se busca una orden dentro del registro de reservaciones registradas.

**Networkx**: Visualizacion de grafo.

- **Prueba Unitaria** pytest
- **Profiling** ProfilerMiddleware
- **Requests** Postman
- **Load Testing** Jmeter

### Cómo ejecutar API
1. Encontrar el file 'app.py' para poder correr el api.
```
cd MovieTicketReservations
```

2. Correr aplicación ejecutando el siguiente comando
```
python3 app.py
```

3. Interactuar con los distintos paths para reservar entradas al cine.

### Cómo ejecutar Profiling
1. Encontrar el file 'profiling.py' para poder correr el api.

2. Correr aplicación ejecutando el siguiente comando
```
python3 profiling.py
```

3. Se va a abrir un nuevo port en el que correrá la aplicación

4. Por cada path por que el usuario interactue, se puede ir viendo el profiling en terminal con el tiempo y cantidad de llamadas por funcion.

5. Para detener el profiling ejecute el siguiente comando:
```
^C
```
### Cómo ejecutar Unit Test
1. Encontrar el file 'test_app.py' para poder correr el api.
```
cd MovieTicketReservations
```

2. Correr aplicación ejecutando el siguiente comando
```
pytest
```

3. Analizar los resultados, todos deberían haber pasado el test

### Recursos
- html template: https://www.w3schools.com/w3css/w3css_templates.asp
- clases NamedTuple: https://realpython.com/python-namedtuple/
- flask: https://www.fullstackpython.com/flask.html
- numpy arrays: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
- presentación proyecto parte 1: https://view.genial.ly/622589a942b168001891a4ef/presentation-movie-ticket-reservation 
- queue: https://www.programiz.com/dsa/queue
- stack: https://www.programiz.com/dsa/stack
- tree: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
- presentación proyecto parte 2: https://view.genial.ly/6272a36e91e2ef0011ffe304/presentation-segunda-entrega-estructuras
- grafo: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
- merge sort: https://www.geeksforgeeks.org/merge-sort/
- jump search: https://www.geeksforgeeks.org/jump-search/
- networkx: https://www.toptal.com/data-science/graph-data-science-python-networkx
- presentación proyecto entrega final: https://view.genial.ly/6282ff68896f3d00111fc569/presentation-business-vision-presentation
