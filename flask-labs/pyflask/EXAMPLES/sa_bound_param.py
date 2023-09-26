
from sqlalchemy import create_engine, Table, MetaData, bindparam

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

metadata = MetaData(bind=engine)

conn = engine.connect()

pres = Table(
    'presidents',
    metadata,
    autoload=True
)

s = pres.select(pres.c.party == bindparam('party'))

results = s.execute(party='Republican')
for row in results:
    full_name = f"{row.firstname} {row.lastname}"
    print(f"{full_name:28s} {row.termstart} {row.birthstate}")

print("---------")
results = s.execute(party='Whig')
for row in results:
    full_name = f"{row.firstname} {row.lastname}"
    print(f"{full_name:28s} {row.termstart} {row.birthstate}")

print("---------")
results = s.execute(party='Federalist')
for row in results:
    full_name = f"{row.firstname} {row.lastname}"
    print(f"{full_name:28s} {row.termstart} {row.birthstate}")
