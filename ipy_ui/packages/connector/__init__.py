from psycopg2 import (
    connect,
    DatabaseError
)
from configparser import ConfigParser

class WorkerSQL:

    def __init__(self, get_settings, settings, section):

        self.get_settings = get_settings
        self.filename = settings
        self.section = section

        self.parser = ConfigParser()
        self.database = dict()
        self.data = dict()

        self.connection = None

    # Прямое подключение к PostgreSQL
    def connectPostgreSQL(self):
        try:
            self.connection = connect(**self.databaseCheck())

            cursor = self.connection.cursor()
            cursor.execute(self.get_settings)

            self.data = cursor.fetchall()
            cursor.close()

            return self.data

        except (Exception, DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()

                # print('\n[+] [SQL] Request : [{0}] completed, connection closed'.format(self.get_settings))
            else:
                pass

    # Проверка файла перед соединением
    def databaseCheck(self):
        self.parser.read(self.filename)

        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            for param in params:
                self.database[param[0]] = param[1]
        else:
            raise Exception('\n[-] File "{0}" not found on "{1}" folder'.format(self.section, self.filename))

        return self.database