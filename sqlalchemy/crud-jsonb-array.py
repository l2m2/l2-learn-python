from sqlalchemy import create_engine, ARRAY, String, cast, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified
from models import Model1

engine = create_engine('postgresql://postgres:postgres@localhost/sqlalchemy-demo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def _demo1():
  m2 = Model1(name="m2", attr_data={"key1": "value1", "key2": "value2"}, tags=["tag1", "tag2", "tag3"])
  session.add(m2)
  session.commit()


def _demo2():
  session.add_all([
    Model1(name="m3", attr_data={
      "key1": "value1",
      "key2": "value2"
    }, tags=["tag1", "tag2", "tag3"]),
    Model1(name="m4", attr_data={
      "key1": "value11",
      "key2": "value22"
    }, tags=["tag1", "tag3"]),
    Model1(name="m5", attr_data={
      "key1": "value111",
      "key2": "value222"
    }, tags=["tag1", "tag2"])
  ])
  session.commit()


def _demo3():
  row = session.query(Model1).filter(Model1.id == 1).one()
  session.delete(row)
  session.commit()


def _demo4():
  rows = session.query(Model1).filter(Model1.attr_data.isnot(None)).all()
  for row in rows:
    print(row)


def _demo5():
  rows = session.query(Model1).filter(Model1.attr_data["key1"].astext == "value1").all()
  for row in rows:
    print(row)


def _demo6():
  rows = session.query(Model1).filter(Model1.tags.any("tag2")).all()
  for row in rows:
    print(row)


def _demo7():
  rows = session.query(Model1).filter(Model1.tags.contains(cast(["tag2", "tag3"], ARRAY(String)))).all()
  for row in rows:
    print(row)


def _demo8():
  # rows = session.query(Model1).update(
  #   {Model1.attr_data: func.jsonb_set(Model1.attr_data if Model1.attr_data else {}, "{key2}", '"value3"')},
  #   synchronize_session=False)
  # session.commit()
  rows = session.query(Model1)
  for row in rows:
    d = {}
    if row.attr_data:
      d = dict(row.attr_data)
    d["key2"] = f'{d["key2"] if "key2" in d else ""}_suffix'
    row.attr_data = d
  session.commit()


def _demo9():
  sql = """
  UPDATE model1
  SET attr_data = jsonb_set(
    COALESCE(attr_data, '{}'::jsonb), 
    '{key2}', 
    concat('"', COALESCE(attr_data->>'key2', ''), '_suffix', '"')::jsonb
  )
  """
  session.execute(sql)
  session.commit()


if __name__ == "__main__":
  _demo9()