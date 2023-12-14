class Personaje:
    def _init_(self, nombre, posicion_x, posicion_y, vidas):
        self.nombre = nombre
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vidas = vidas

    def mover(self, direccion):
        print(f"{self.nombre} se mueve hacia {direccion}")

    def saltar(self, altura):
        print(f"{self.nombre} salta {altura} metros")

    def caer(self):
        print(f"{self.nombre} cae al suelo")


class Mario(Personaje):
    def lanzar_fuego(self):
        print(f"{self.nombre} lanza una bola de fuego")


class Luigi(Personaje):
    def usar_hongo(self):
        print(f"{self.nombre} usa un hongo para crecer")


class Enemigo:
    def _init_(self, tipo, posicion_x, posicion_y, daño):
        self.tipo = tipo
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.daño = daño

    def mover(self, direccion):
        print(f"{self.tipo} se mueve hacia {direccion}")

    def atacar(self, objetivo):
        print(f"{self.tipo} ataca a {objetivo}")


class KoopaTroopa(Enemigo):
    def usar_casco(self):
        print(f"{self.tipo} usa su caparazón como arma")


class Goomba(Enemigo):
    def saltar(self):
        print(f"{self.tipo} salta hacia {self.posicion_x+1}, {self.posicion_y}")