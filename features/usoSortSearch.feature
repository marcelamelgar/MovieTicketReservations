@usoSortSearch
# fourteenth feature
Feature: Usar jump search para buscar un número de órden

	Scenario: Cambien el search por medio del tree a Jump Search
      Given los números de órden
      Then aplicarles un Merge Sort para poder ordenar las órdenes
      And poder implementar la nueva estructura de búsqueda Jump Search