import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

data_base_type = '////'
user_name = '////'
pass_word = '////'
host = 'localhost'
host_port = '5432'
data_base_name = '////'

DSN = f'{data_base_type}://{user_name}:{pass_word}@{host}:{host_port}/{data_base_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_shops(publisher_data):
    model_query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop). \
        join(Stock). \
        join(Book). \
        join(Publisher). \
        join(Sale)
    if publisher_data.isdigit() is True:
        item = model_query.filter(publisher_data == Publisher.id).all()
    else:
        item = model_query.filter(publisher_data == Publisher.name).all()
    for name_book, name_shop, price_sell, data_sell in item:
        print(f'{name_book} | {name_shop} | {price_sell} | {data_sell.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    input_data = input()
    get_shops(input_data)
session.close()
