@searchOrder
# eighth feature
Feature: Ver la información de reservación de un cliente en base a su número de orden

	Scenario: El empleado puede ver el número de orden de una reservación
	  Given el número de orden asignado a cada reservación
	  Then el empleado puede ver la información de reservación
      And tiene la opcion de cancelar o eliminar la orden si el cliente desea