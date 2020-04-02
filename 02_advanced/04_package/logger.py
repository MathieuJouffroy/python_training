import time
import os.path
import getpass
import logging
from os import path
from random import randint
from functools import wraps

logging.basicConfig(format='%(message)s', filename='machine.log', filemode='w', level=logging.INFO)
# %(message)s -> to filter out "INFO:root:"

def log(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        user = getpass.getuser()
        logging.info(f"({user})Running: {method.__name__.capitalize()}\t\t"
        + f"[ exec-time = {end - start:.3f} ms ]")
        return result
    return timed

class CoffeeMachine():

    water_level = 1000

    @log
    def start_machine(self):
      if self.water_level > 20:
          return True
      else:
          print("Please add water!")
          return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
	
	machine = CoffeeMachine()
	for i in range(0, 5):
		print ('-------NEW-------')
		machine.make_coffee()
	
	print ('-------NEW-------')
	machine.make_coffee()
	print ('-------NEW-------')
	machine.add_water(70)


