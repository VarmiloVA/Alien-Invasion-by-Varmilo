# Alien-Invasion-by-Varmilo
The Alien Invasion game using Python and the pygame package.

In general: In Alien Invasion, the player controls the mothership. The player can control the mothership either  with WASD keysor the arrows for moving, and left mouse click for shooting. The player needs to destroy the ufos that are moving, if the user loses 3 lives the game is over 


To do: 

-Levels: the difficulty of the level will be based on the speed of the mothership and the speed of the ufos. 

-Main menu in which you can play two game modes: levels and custom. In "levels" you will have ~15 levels, when you complete all of them you will be able to use additional features and various skins. In custom you can select your speed and the enemy's speed. 

-Cosmetic products: when you have completed the ~15 levels, every bullet you shoot will be in a different color and you will be able to select the game background color.


The code is completed up to this point. Next steps are up to the user ;)

The biggest issue, THE ENEMY 'S MOVEMENT! (How to resolve the problem) 

(Sorry but this part will be in spanish 'cause I'm not sure how much sense will have this paragraph in spanish, so if I write it in english it will be extremely confusing) 

Hay que tratar cada nave como un objeto independiente y no como un sprite, para hacer el tipo de movimiento que quiero, usando esta lógica, tendré que aprender a usar la librería que maneja el tiempo, aunque no creo que esta demasiado difícil, una vez sabiendo manejar esta librería, tendré que hacer que cuando le des a la tecla espacio se organizen las flotas en la pantalla y cuando terminan de organizarse que se paren, comience el juego y que las flotas en pantalla comienzen a moverse de forma aleatoria (biblioteca rando imagino) pero al chocar con otros ovnis o al chocar con los borde de la pantalla cambien de dirección, pero si chocan con la nave del jugador hacer que este se le reste una de las tres vidas que tiene.
Every ufo needs to be treated as an independent object and not as part of a Sprite.
