#!/usr/bin/env python3

import pickle
import datetime

now = datetime.datetime.now()

filename = 'data'

outfile = open(filename,'wb')
pickle.dump(now,outfile)
outfile.close()

infile = open(filename,'rb')
new_datetime = pickle.load(infile)
infile.close()

print(new_datetime)
