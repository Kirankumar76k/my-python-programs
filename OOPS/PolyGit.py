class Artillery():
    def __init__(self):
        self.className = "Artillery Class constructor"

    def showName(self):
        shootingRange = "aprox. 1-30 km"
        return "Artillery" + " " + shootingRange


class Mortar(Artillery):
    def showName(self):
        shootingRange = "1 km"
        return "Mortar" + " " + shootingRange


class Howitzer(Artillery):
    def __init__(self):
        self.className = "Howitzer Class constructor"
        self.rndMath = 2 * 2

    def showName(self, color="Green"):
        shootingRange = "35 km"
        return "Howitzer " + color + " " + shootingRange


class Cannon(Artillery):
    def showName(self):
        shootingRange = "10 km"
        return "Cannon" + " " + shootingRange


a = Artillery();
print(a.className)
print(a.showName())
print("\n")

m = Mortar();
print(m.className)
print(m.showName())
print("\n")

h = Howitzer();
print(h.className)
print(h.rndMath)
print(h.showName())
print("\n")

x = Howitzer();
print(x.className)
print(x.rndMath)
print(x.showName("Blue"))
print("\n")

c = Cannon();
print(c.className)
print(c.showName())
print("\n")