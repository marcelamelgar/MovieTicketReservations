@reservation
# fourth feature
Feature: Llevar a cabo la reservación de las entradas
	
    Scenario: El cliente ingresa sus datos para reservar entradas
      Given la película
      And el horario disponible escogido
      And cantidad de entradas
      And asientos elegidos
      Then el cliente ingresa los datos de reservación tales como nombre y forma de pago