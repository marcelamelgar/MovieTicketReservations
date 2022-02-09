@chooseSeats
# third feature
Feature: Escoger los asientos que se desean reservar

	Scenario: El cliente ve los asientos disponibles y escoge el que prefiera
	  Given la película 
	  And el horario que eligió el cliente
	  Then el cliente elige la cantidad de asientos que quiere reservar
	  And escoge entre los disponibles, los que reservará