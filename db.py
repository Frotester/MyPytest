from sqlalchemy.orm import sessionmaker

from sqlalchemy import  create_engine

from sqlalchemy.ext.declarative import declarative_base
from configuration import CONNECTION_ROW

Model = declarative_base(name='Model')

engine = create_engine(
    CONNECTION_ROW
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

session = Session()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Добавляем нового пользователя
# cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('Nad16', 'newuser16@example.com', 16))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()


