@chooseMovie
# first feature
Feature: Escoger la película en la cual se quieren reservar entradas

	Scenario: Cliente puede ver la cartelera y escoger la película
	  Given el cliente ve la cartelera de películas
	  When el cliente escoge una película para ver su información
	  Then el cliente tiene la opción de reservar tickets para esa película