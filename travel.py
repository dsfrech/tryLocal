# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        #if self.time != 0:
        return self.odometer / self.time
        # else:
        #     pass

if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("what should I do? [a]ccelerate, [b]rake, "
                       "show [o]dometer, or show average [s]peed, or [q]uit?").upper()
        if action not in "ABOSQ" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == "Q":
            break
        if action == "A":
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
