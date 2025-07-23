from db import session

import tables

from sqlalchemy.sql.expression import desc


# res = session.query(
#     tables.Users.username, tables.Users.email
# ).filter(
#     tables.Users.age > 10,
#     tables.Users.age < 27,
# ).all()
# print(res)

res = session.query(
    tables.Users.age
).filter(
    tables.Users.age > 1
).order_by(desc(tables.Users.age)).limit(1).offset(3).all()
print(res)


# if res:
#     print("All is good")
# else:
#     print("Not good")

# res = session.query(
#     tables.Users.username, tables.Users.email
# ).first()
# print(res)
