import random

DS_SCIENTISTS = None

ADJS = [
  'cunning'
  'clever',
  'witty'
 
]


def get_random_name_id():
  adj = ADJS[random.randint(0, len(ADJS)-1)
  scientist = DS_SCIENTISTS[random.randint(0, len(DATA_SCIENTISTS)-1)]
  return f'{adj}_{scientist}'
  
