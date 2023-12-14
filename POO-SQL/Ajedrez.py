class Pieza:
    def _init_(self, color, posicion):
        self.color = color
        self.posicion = posicion

    def capturar(self):
        print("La pieza ha sido capturada.")


class Peon(Pieza):
    def avanzar(self):
        print("El peón avanza hacia adelante.")


class Torre(Pieza):
    def moverse(self):
        print("La torre se mueve en línea recta por filas o columnas.")


class Alfil(Pieza):
    def moverse(self):
        print("El alfil se mueve en línea diagonal.")


class Caballo(Pieza):
    def moverse(self):
        print("El caballo se mueve en forma de L.")


class Reina(Pieza):
    def moverse(self):
        print("La reina se mueve en línea recta, horizontal y diagonal.")


class Rey(Pieza):
    def moverse(self):
        print("El rey se mueve en cualquier dirección, pero solo una casilla a la vez.")


class Tablero:
    def _init_(self):
        self.piezas = []

    def agregar_pieza(self, pieza):
        self.piezas.append(pieza)

    def dibujar(self):
        print("Estado actual del tablero:")
        for pieza in self.piezas:
            print(f"Pieza: {type(pieza)._name_}, Color: {pieza.color}, Posición: {pieza.posicion}")