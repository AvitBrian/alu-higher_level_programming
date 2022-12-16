object relational mapping here!

# Background Context
Now there are two ways of doing this... 
one, using the module MySQLdb to connect to a MySQL database and execute your SQL queries manually.
Orrrr, use the module SQLAlchemy (the ORM).the Object Relational Mapper will abstract the storage to the 
usage. So this way we get to use just python, and forget the boring SQL stuff.

### Connecting with MySQLdb:

```
connection = MySQLdb.connect(
                        host="localhost", 
                        port=3306,
                        user="root", 
                        passwd="root", 
                        db="my_db", 
                        charset="utf8")
with connection.cursor() as cursor:
    curser.execute("SELECT * FROM states ORDER BY id ASC")
    result = curser.fetchall()
    for row in result:
        print(row)
connection.close()
```

### Using SQAlchemy: 
```
    with create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format("root", "root", "my_db"), 
                    pool_pre_ping=True) as engine:                
        Base.metadata.create_all(engine)
        with Session(engine)as session:
            for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))

