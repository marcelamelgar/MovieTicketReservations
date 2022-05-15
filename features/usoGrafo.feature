@usoGrafo
# thirteenth feature
Feature: Usar un grafo en mi código

	Scenario: Puedo usar un grafo para la distribución de horarios y salas con las películas
      Given las películas
      And el array con los horarios de cada película
      And el array con los horarios asignados a cada sala
      Then hacer un grafo que los conecte con sus significativas películas, horarios y sala
      And horarios y sala tiene que ser un loop de dirección para accederlos en feature 11 y 12