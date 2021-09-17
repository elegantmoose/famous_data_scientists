import csv
import random


DS_SCIENTISTS_FP = 'famous_data_scientists.csv'
COOL_ADJS_FP = 'cool_adjs.txt'
DS_SCIENTISTS = None
COOL_ADJS = None


def get_random_name_id():
  adj = COOL_ADJS[random.randint(0, len(COOL_ADJS)-1)
  scientist = DS_SCIENTISTS[random.randint(0, len(DATA_SCIENTISTS)-1)]
  return f'{adj}_{scientist}'

             
def _init():
    with open(COOL_ADJS_FP, 'r') as fh:
        COOL_ADJS = fh.readlines()
    with open(DS_SCIENTISTS_FP, 'r') as csv_fh:
        DS_SCIENTISTS = [row['name'] for row in csv.DictReader(csv_fh, delimiter=';')]


_init()
