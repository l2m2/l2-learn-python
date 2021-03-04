from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from models import Base, User

engine = create_engine('postgresql://postgres:postgres@localhost/sqlalchemy-demo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def _create1():
  user1 = User(username="leon", fullname="李黎明", email="l2m2lq@gmail.com", password="123456")
  user2 = User(username="ronaldo", fullname="罗纳尔多", email="ronaldo@gmail.com", password="123456")
  session.add(user1)
  session.add(user2)
  session.commit()


def _create2():
  session.add_all([
    User(username="cat", fullname="王二猫", email="cat@gmail.com", password="123456"),
    User(username="dog", fullname="张晓狗", email="dog@gmail.com", password="123456"),
    User(username="pig", fullname="刘大猪", email="pig@gmail.com", password="123456")
  ])
  session.commit()


def _query1():
  items = session.query(User).order_by(User.id)
  for item in items:
    print(repr(item))


def _query2():
  for username in session.query(User.username):
    print(username)


def _query3():
  for row in session.query(User.username.label("name_label")).all():
    print(row.name_label)


def _query4():
  for row in session.query(User).order_by(User.username.desc()).all():
    print(row)


def _query5():
  for row in session.query(User).filter(User.fullname.like("李%")).all():
    print(row)


def _query6():
  row = session.query(User).filter(func.length(User.username) == 3).order_by(User.username).first()
  print(row)


def _query7():
  row = session.query(User.id, User.username).filter(func.length(User.username) == 4).scalar()
  print(row)


def _delete1():
  row = session.query(User).filter(User.username == "leon").one()
  session.delete(row)
  session.commit()


def _update1():
  row = session.query(User).filter(User.username == "pig").one()
  row.username = 'pig1'
  session.commit()


if __name__ == "__main__":
  _update1()