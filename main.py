from pet import Pet

import random
# from config import START_HUNGER, START_HAPPY, START_ENERGY
import config

choco = Pet("초코")
print(choco)

print("pet.py 의 __name__:", __name__)

def __init__(self, name):
    self.name = name   # 이름
    self.hunger = START_HUNGER   # 배고픔 (0 ~ 100)
    self.happy = START_HAPPY    # 행복도 (0 ~ 100)
    self.energy = START_ENERGY   # 에너지 (0 ~ 100)
    self.alive = True  
    Pet.count += 1