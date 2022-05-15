@viewSala
# eleventh feature
Feature: Ver en qué sala está un horario de película

	Scenario: El cliente quiere ver qué sala es su película
      Given la película
      And el horario disponible escogido
      Then buscar en qué sala está el horario asignado