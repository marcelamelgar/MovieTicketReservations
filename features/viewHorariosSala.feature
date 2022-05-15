@viewHorariosSala
# twelfth feature
Feature: Ver qué horarios tiene asignada alguna sala

	Scenario: El administrador del cine quiere saber qué horarios tiene asignada una sala
      Given la sala
      And los horarios asignados
      Then buscar en qué horarios están asignados para la sala