# Alien-Invasion-by-Varmilo
The Alien Invasion game made using Python and the pygame library

In general:
In Alien Invasion, the player controls a mothership. The player can control the mothership
with WASD or the arrows for moving and left mouse click for shooting. The player needs to
destroy the ufos that are moving, if the user lose 3 lives the game will finish.

To do:
-Dificult levels, the dificult of the level will be based in the speed of the mothership
and the speed of the ufos.
-Main menu in which you can play two gamemodes: levels and custom. In "levels" you will
have ~15 levels, when you complete all of them you will be abled to use cosmetic products. In
custom you can select your speed and the enemy's speed.
-Cosmetic products: when you have completed the ~15 levels, every bullet you shoot will be
in a different color and you will be abled to select the game background color.

The biggest issue, THE ENEMY'S MOVEMENT! (How to resolve the problem) (ES)
(Sorry but this part will be in spanish 'cause I not sure how much sense will have this 
paragraph in spanish, so if I write it in english it will be extremely confusing)
Hay que tratar cada nave como un objeto independiente y no como un sprite, para hacer el
tipo de movimiento que quiero, usando esta lógica, tendré que aprender a usar la librería
que maneja el tiempo, aunque no creo que esa demsiado difícil, una vez sabiendo manejar esta
librería, tendré que hacer que cuando le des a la tecla espacio se organizen las flotas en la 
pantalla y cando terminan de organizarse que se paren, comience el juego y que las flotas en
pantalla comienzen a moverse de forma aleatoria (biblioteca rando imagino) pero al chocar 
con otros ovnis o al chocar con los borde de la pantalla cabien de dirección, pero si chocan
con la nave del jugador hacer que este se le reste una de las tres vidas que tiene.
