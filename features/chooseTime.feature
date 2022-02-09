@chooseTime
# second feature
Feature: Escoger horario de la película 
	
    Scenario: Cliente puede escoger horario y asientos para reservar
      Given la película escogida por el cliente
      Then el cliente puede escoger el horario que prefiera dentro de los disponibles.