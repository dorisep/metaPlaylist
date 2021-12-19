from pathlib import Path
import sqlite3

class SQLite:
    """
    A minimal sqlite3 context handler that removes pretty much all
    boilerplate code from the application level.
    """

    def __init__(self, path: Path):
        self.path = path

    def __enter__(self):
        self.connection: sqlite3.Connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        # do not forget this or you will not be able to use methods of the
        # context handler in your with block
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


