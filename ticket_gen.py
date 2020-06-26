from __future__ import print_function

import re
import sys
import argparse
import numpy as np
import json # json.dumps to encode
import copy
import pandas as pd
from pandas.io.json import json_normalize
import string
import datetime
import time
from dateutil.parser import parse as parse_datetime

from random import *

# Set default variables values
STATUS_VALUES = ["Open", "Closed", "Resolved", "Waiting for Customer", "Waiting for Third Party", "Pending"]
ACTIVITY_FORMAT = {
  "shipping_address": str,
  "shipment_date": datetime.datetime,
  "category": str,
  "contacted_customer": bool,
  "issue_type": str,
  "source": int,
  "status": str,
  "priority": int,
  "group": str,
  "agent_id": int,
  "requester": int,
  "product": str
}
TICKET_FORMAT = {
  "performed_at": datetime.datetime,
  "ticket_id": int,
  "performer_type": "user",
  "performer_id": 149018,
  "activity": ACTIVITY_FORMAT
}

# Random functions
def str_time_prop(start, end, format, prop):
  stime = time.mktime(time.strptime(start, format))
  etime = time.mktime(time.strptime(end, format))
  ptime = stime + prop * (etime - stime)
  return time.strftime(format, time.localtime(ptime))

def random_date(start="01-01-2000 01:00:00", end="25-06-2020 01:00:00", prop=random(), format="%d-%m-%Y %H:%M:%S"):
  return str_time_prop(start, end, format, prop)

def random_string(length=8):
  letters = string.ascii_lowercase
  return ''.join(choice(letters) for i in range(length))

# Process function
def gen_ticket(id=1):
  t = copy.deepcopy(TICKET_FORMAT)
  t["performed_at"] = random_date(prop = random())
  t["ticket_id"] = id+100
  t["activity"]["shipping_address"] = "N/A"
  t["activity"]["shipment_date"] = random_date("01 Jan, 2000", "25 Jun, 2020", random(), "%d %b, %Y")
  t["activity"]["category"] = random_string(5)
  t["activity"]["contacted_customer"] = bool(getrandbits(1))
  t["activity"]["issue_type"] = random_string(8)
  t["activity"]["source"] = randint(1,10)
  t["activity"]["status"] = choice(STATUS_VALUES)
  t["activity"]["priority"] = randint(1,10)
  t["activity"]["group"] = random_string(6)
  t["activity"]["agent_id"] = randint(100000, 200000)
  t["activity"]["requester"] = randint(100000, 200000)
  t["activity"]["product"] = random_string(6)
  return t

def get_ticket(start=1, stop=1000):
  for id in range(start, stop+1):
    yield gen_ticket(id)

def write_activity_json(o_file, data):
  with open(o_file, 'w') as outfile:
    json.dump(data, outfile)

# Execute function
def run(argv=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', required=True, nargs='?', const=10, type=int, help="Generate n tickets with random activities.")
  parser.add_argument('-o', required=True, nargs='?', const="activities.json", type=str, help="Output file name.")
  known_args = parser.parse_args(argv)
  # Gen tickets
  tickets = [ticket for ticket in get_ticket(1, known_args.n)]
  # Write to json file
  write_activity_json(known_args.o, tickets)


if __name__ == '__main__':
  run()