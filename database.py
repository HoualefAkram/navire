import mysql.connector
import random
import string
from tkinter import messagebox


class DatabaseService:
    def __init__(self) -> None:
        self.db = None
        self.cursor = None

    def _connectToDatabase(self) -> None:
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="0777910785",
            database="navireDB",
        )
        self.cursor = self.db.cursor()

    def _create_table(self) -> None:
        if not self.cursor:
            self._connectToDatabase()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS ships (id CHAR(20) NOT NULL PRIMARY KEY,owner CHAR(50) NOT NULL ,type CHAR(20) NOT NULL, height CHAR(50) NOT NULL, width CHAR(50) NOT NULL, charge CHAR(50) NOT NULL, propultion CHAR(20) NOT NULL, initial_date CHAR(20) NOT NULL)"
        )

    def initilize(self):
        self._create_table()

    @staticmethod
    def _generate_random_id():
        length: int = 10
        characters = string.ascii_letters + string.digits
        random_id = "".join(random.choice(characters) for _ in range(length))
        return random_id

    @staticmethod
    def _isAllowed(
        owner,
        ship_type,
        height,
        width,
        charge,
        propultion,
    ) -> bool:
        return (
            len(owner) > 1
            and len(ship_type) > 1
            and len(height) > 1
            and len(width) > 1
            and len(charge) > 1
            and len(propultion) > 1
        )

    def register_ship(
        self,
        owner,
        ship_type,
        height,
        width,
        charge,
        propultion,
        initial_date,
    ):
        if not self._isAllowed(
            owner,
            ship_type,
            height,
            width,
            charge,
            propultion,
        ):
           messagebox.showwarning('Error', 'Invalid input!')
           return;
        ship_id: str = self._generate_random_id()
        command = "INSERT INTO ships (id, owner, type, height, width, charge ,propultion, initial_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            ship_id,
            owner,
            ship_type,
            height,
            width,
            charge,
            propultion,
            initial_date,
        )
        self.cursor.execute(command, values)
        self.db.commit()
        print("Successful")
