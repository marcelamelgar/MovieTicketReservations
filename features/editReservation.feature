@editReservation
# sixth feature
Feature: Editar los datos de la reservación realizada

	Scenario: Al cliente no le parece su reservación y desea editarla
	  Given el desacuerdo con la reservación realizada previamente
	  When el cliente le da "editar reservación"
	  Then el cliente puede hacer cambios a la reservación
	  And confirmar cuando esté de acuerdo con la reservación