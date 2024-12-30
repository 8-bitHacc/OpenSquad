import sqlite3, json, traceback
from threading import Lock
from Classes.Instances.PlayerInstance import PlayerInstance

class SQLiteManager:
    def __init__(self):
        """Creates an instance of SQLiteManager and prepares the database"""
        self.connection: sqlite3.Connection = sqlite3.connect("Classes/DataBase/Entries/players.sqlite", check_same_thread=False)
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        self.mutex: Lock = Lock()
        try:
            self.connection.execute(f"CREATE TABLE IF NOT EXISTS playerTable (HighID integer, LowID integer, AuthenticationToken text, Data json)")
        except (sqlite3.ProgrammingError, Exception) as e:
            print(f"An exception has occurred while trying to set up the playerTable database. Error: {e}")

    def createEntry(self, auth: str, data: dict):
        """Creates an entry to the database and updates it"""
        self.mutex.acquire()
        try:
            self.cursor.execute(f"INSERT INTO playerTable (HighID, LowID, AuthenticationToken, Data) VALUES (?, ?, ?, ?)",
                                (*data["PlayerID"], auth, json.dumps(data, ensure_ascii=False)))
            self.connection.commit()
        except (sqlite3.ProgrammingError, Exception) as e:
            print(f"An exception has occurred while trying to create an entry. Error: {e}")
        finally:
            self.mutex.release()

    def getEntry(self, auth: str, acMutex: bool = True) -> dict:
        if acMutex: self.mutex.acquire()
        try:
            self.cursor.execute("SELECT Data FROM playerTable WHERE AuthenticationToken = ?", (auth,))
            return json.loads(self.cursor.fetchone()[0])
        except (sqlite3.ProgrammingError, Exception) as e:
            print(f"An exception has occurred while trying to get an entry. Error: {e}")
        finally:
            if acMutex: self.mutex.release()

    def updateEntry(self, item: list[str] | str, value, auth: str = None, data: dict = None):
        """Updates an entry on a specific item with the updated value and saves it into the database"""
        with self.mutex:
            try:
                if data is None: entry = self.getEntry(auth, False)
                else:
                    entry = data
                    auth = data["AuthenticationToken"]

                if isinstance(item, list):
                    for i, key in enumerate(list): entry[key] = value[i]
                else:
                    entry[item] = value

                entry = {key: value for key, value in entry.items() if value not in [None, "", {}, [], False, 0]}

                self.cursor.execute("UPDATE playerTable SET Data = ? WHERE AuthenticationToken = ?", (json.dumps(entry, ensure_ascii=False), auth,))
                self.connection.commit()
            except (sqlite3.ProgrammingError, Exception) as e:
                print(traceback.print_exc())
                print(f"An exception has occurred while trying to save an entry. Error: {e}")

    def incrementID(self):
        with self.mutex:
            try:
                self.cursor.execute("SELECT HighID, LowID FROM playerTable ORDER BY HighID DESC, LowID DESC")
                result = self.cursor.fetchone()

                if result:
                    HighID, LowID = result
                    LowID += 1

                    if LowID % 100 == 0:
                        HighID += 1
                        LowID = LowID

                else:
                    HighID, LowID = 0, 1

                return [HighID, LowID]
            except:
                print('erro')
                return [0, 1]