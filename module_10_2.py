from time import sleep
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 100
        total = 0
        while i:
            sleep(1)
            i -= self.power
            total += 1
            print(f'\n {self.name} сражается {total} дней(дня)..., осталось {i} воинов."')

        print(f'\n {self.name} одержал победу спустя {total} дней(дня)!"')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()



