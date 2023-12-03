import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from Models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:9162784@localhost:5432/test2'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
input_name = "O\u2019Reilly"
# input_name = "Pearson"
# input_name = "Microsoft Press"
# input_name = "No starch press"

id_publisher_subquery = session.query(Publisher).filter(Publisher.name == input_name).subquery()
for data_book in session.query(Book).join(id_publisher_subquery,
                                    Book.id_publisher == id_publisher_subquery.c.id).all():
    name_book = data_book
    data_stock_subquery = session.query(Stock).filter(Stock.id_book == name_book.id).subquery()
    for data_shop in session.query(Shop).join(data_stock_subquery, Shop.id == data_stock_subquery.c.id_shop):
        name_shop = data_shop
        for data_sale in session.query(Sale).join(data_stock_subquery, Sale.id_stock == data_stock_subquery.c.id):
            print(f'{name_book} | {name_shop} | {data_sale.price} | {data_sale}')


# for data in session.query(Publisher).all():
#     print(data)
# for data in session.query(Shop).all():
#     print(data)
# for data in session.query(Sale).all():
#     print(data)


session.close()
