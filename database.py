from sqlalchemy import create_engine

url = 'mysql+mysqlconnector://root:9j9wrld9@localhost/qalakriti'

engine = create_engine(url, echo=True)
connection = engine.connect()

# engine = create_engine("mysql+mysqlconnector://user:password@host/database")