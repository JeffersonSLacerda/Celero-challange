import argparse
import csv
from tqdm import tqdm
from django.db import transaction

from olimpics.models import Athlete 

def get_file_number_lines(filepath):
  with open(filepath) as f:
    return sum(1 for _ in f)

def parse_number(value):
  try:
      return int(value)
  except ValueError:
      try:
          return float(value)
      except ValueError:
          return None

@transaction.atomic
def run(*args):
  parser = argparse.ArgumentParser(description="Populate database based in a csv file")
  parser.add_argument('file_path', type=str, help='file path to csv file')

  args = parser.parse_args(args)
  num_lines = get_file_number_lines(args.file_path)
 
  with open(args.file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    _header = next(reader)
    
    athletes = [None]*1024
    athletes_size = 0

    for row in tqdm(reader, total=num_lines-1):      
      athletes[athletes_size] = Athlete(
        athlete_id = row[0],
        name = row[1],
        sex = row[2],
        age = parse_number(row[3]),
        height = parse_number(row[4]),
        weight = parse_number(row[5]),
        team = row[6],
        noc = row[7],
        games = row[8],
        year = row[9],
        season = row[10],
        city = row[11],
        sport = row[12],
        event = row[13],
        medal = row[14]
      )
      
      athletes_size += 1
      
      if athletes_size == 1024:
        Athlete.objects.bulk_create(athletes)
        athletes_size = 0
        
    if athletes_size > 0:
        Athlete.objects.bulk_create(athletes[:athletes_size])