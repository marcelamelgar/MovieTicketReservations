@assingOrderNumber
# seventh feature
Feature: Asignarle un numero de orden a cada reservación que se lleve a cabo

	Scenario: El cliente optiene un número único de orden para su reservación
	  Given una reservación realizada
	  Then el cliente obtiene un número único de orden