import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale
data_base_type = '///'
user_name = '////'
pass_word = '///'
host = 'localhost'
host_port = '5432'
data_base_name = '////'

DSN = f'{data_base_type}://{user_name}:{pass_word}@{host}:{host_port}/{data_base_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

session.close()
