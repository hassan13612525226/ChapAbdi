import sqlite3
from config import DB_NAME


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = connect()
    cur = conn.cursor()

    # ==========================
    # مشتریان
    # ==========================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        phone TEXT,

        address TEXT

    )
    """)

    # ==========================
    # سفارش ها
    # هر فاکتور فقط یک رکورد
    # ==========================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_id INTEGER,

        total_price REAL DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # ==========================
    # اقلام هر فاکتور
    # ==========================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        order_id INTEGER,

        service TEXT,

        quantity REAL,

        unit TEXT,

        unit_price REAL,

        total_price REAL

    )
    """)

    # ==========================
    # تنظیمات
    # ==========================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings(

        key TEXT PRIMARY KEY,

        value TEXT

    )
    """)

    defaults = {

        "پلات":"200000",

        "ترنسپرنت":"850000",

        "پرت رول":"400000",

        "کپی یک رو سیاه سفید":"700",

        "کپی دو رو سیاه سفید":"1200",

        "پرینت رنگی یک رو":"6000",

        "پرینت رنگی دو رو":"10000"

    }

    for key,value in defaults.items():

        cur.execute(
            """
            INSERT OR IGNORE
            INTO settings(key,value)
            VALUES(?,?)
            """,
            (key,value)
        )

    conn.commit()
    conn.close()


create_tables()