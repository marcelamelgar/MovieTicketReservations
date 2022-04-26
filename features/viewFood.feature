@viewFood
# nineth feature
Feature: Se pueden ver las diferentes opciones que tiene el cine de comida

	Scenario: El cliente quiere ver que paquetes de comida puede comprar para su función
	  Given las opciones de comida con la que cuenta el cine
	  And el cliente desea ver las opciones
	  Then el cliente puede ingresar al apartado y visualizar las opciones de comida que hay