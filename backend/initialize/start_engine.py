# the database creation

import sqlalchemy
from sqlalchemy import create_engine

metadata = MetaData()

engine = create_engine('localhost:5000/working_schema')
metadata.create_all(engine)

#with engine.connect() as con:
#    rs = con.execute('SELECT * FROM tablename')
#    for row in rs:
#        print row

file = open('raw.sql', 'r')
Lines = file.readlines()

for line in Lines:
    with engine.connect() as con:
        con.execute(line)

file.close()

#
