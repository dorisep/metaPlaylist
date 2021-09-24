import sqlite3

class DBconnection:
    instance = None

    def __new__(cls: Type[_T]) -> _T:
        conn = sqlite3.connect('mysqlite.db')
        c = conn.cursor()
        pass