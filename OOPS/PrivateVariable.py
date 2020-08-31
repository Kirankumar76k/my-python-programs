class Car:

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed),'name='+self.__name)


redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.__name="hige"
redcar.drive()