@confirmReservation
# fifth feature
Feature: Confirmar reservación 

	Scenario: El cliente puede ver los datos de su reservación y confirmar
      Given la película
      And el horario disponible escogido
      And cantidad de entradas
      And asientos elegidos
      And los datos de la reservación
      Then El cliente puede ver los datos completos de su reservación
      And si está de acuerdo, confirmar si estos son correctos
      But si está en desacuerdo, poder editar el dato que no le parece