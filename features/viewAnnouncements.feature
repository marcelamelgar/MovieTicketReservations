@viewAnnouncements
# tenth feature
Feature: El cine quiere promocionar proximas peliculas que se encontraran en cartelera

	Scenario: El cliente esta navegando en la pagina de cartelera y ve los anuncios de próximas películas
	  Given los anuncios de próximas películas
	  And el cliente se encuentra en la página de cartelera
	  Then el cliente puede ver los anuncios de próximas películas que se podrán ver en el cine