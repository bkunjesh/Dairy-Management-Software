import sqlite3
import datetime
import os

# print(datetime.date.today())
year = datetime.date.today().year

def make_connection():
    # year = "2022"

    filename = 'customers.db'

    data_path = "D:\\project\\kaalindi app\\database\\"+str(year)+"\\"

    
    madeNewDir=False;
    if not os.path.exists(data_path):
        os.makedirs(data_path)
        madeNewDir=True

    conn = sqlite3.connect(data_path + filename)
    c=conn.cursor()
    
    tempfilename = 'template.db'
    tempDbDir = "D:\\project\\kaalindi app\\database\\"+tempfilename

    if not madeNewDir:
        isemptyQuery = "SELECT count(*) FROM customer"
        cursor = c.execute(isemptyQuery)
        size = cursor.fetchone()
        if int(size[0]) == 0:
            madeNewDir = True
            deleteQuery = "DROP TABLE customer;"
            c.execute(deleteQuery)

    tempDbPath = "'D:\\project\\kaalindi app\\database\\"+tempfilename+"'"
    attachtempDbQuery = "ATTACH " + tempDbPath + " AS temp_db;"
    

    # print(madeNewDir)

    if os.path.isfile(tempDbDir) and madeNewDir:
        c.execute(attachtempDbQuery)

        

        copyTableQuery = "CREATE TABLE customer AS SELECT * FROM temp_db.customer;"
        c.execute(copyTableQuery)

        detachQuery = "DETACH DATABASE 'temp_db';"
        c.execute(detachQuery)
        print("copied template database.")

    create_customer_table = """CREATE TABLE IF NOT EXISTS customer (
        id INTEGER,
        name	TEXT,
        address	TEXT,
        phone	TEXT,
        regular_morning_quantity	INTEGER,
        regular_morning_rate	INTEGER,
        regular_evening_quantity	INTEGER,
        regular_evening_rate	INTEGER,
        pending_amount	INTEGER,
        credit	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
    ); """

    dairy_table = """CREATE TABLE IF NOT EXISTS "dairy_buy" (
    "d_id"	INTEGER NOT NULL UNIQUE,
    "name"	TEXT,
    "address"	TEXT,
    "morning quantity"	REAL,
    "morning_rate"	REAL,
    "evening_quantity"	REAL,
    "evening_rate"	REAL,
    PRIMARY KEY("d_id" AUTOINCREMENT)
    ) """

    transaction_table = """CREATE TABLE IF NOT EXISTS "item_transaction" (
    "transaction_id"	INTEGER NOT NULL UNIQUE,
    "customer_id"	INTEGER,
    "day"	INTEGER,
    "month"	INTEGER,
    "year"	INTEGER,
    "quantity"	REAL,
    "price"	REAL,
    "shift"	TEXT,
    PRIMARY KEY("transaction_id" AUTOINCREMENT)
    ) """
    
    payment_table = """CREATE TABLE IF NOT EXISTS "payment" (
    "payment_id"	INTEGER NOT NULL UNIQUE,
    "customer_id"	INTEGER,
    "payment_date"	TEXT,
    "payment_amount"	INTEGER,
    PRIMARY KEY("payment_id" AUTOINCREMENT)
    ) """
    

    try:
        c.execute(create_customer_table)
    except Exception as e:
        print(e)
    try:
        c.execute(dairy_table)
    except Exception as e:
        print(e)
    try:
        c.execute(transaction_table)
    except Exception as e:
        print(e)
    try:
        c.execute(payment_table)

    except Exception as e:
        print(e)

    print("succsesfully conected to DB.")

    
    conn = sqlite3.connect(data_path + filename)

    return conn


# make_connection()
