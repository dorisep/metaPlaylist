import sqlite3

class DBconnection:
    instance = None

    def __new__(cls: Type[_T]) -> _T:
        pass