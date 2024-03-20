# -*- coding: utf-8 -*-

from configparser import ConfigParser
from psycopg2 import (
    connect,
    DatabaseError,
)
from logging import (
    error,
    info,
)


class WorkerSQL:

    def __init__(self, get_settings, settings, section):

        self.get_settings = get_settings
        self.filename = settings
        self.section = section

        self.parser = ConfigParser()
        self.database = dict()
        self.data = dict()

        self.connection = None

    def __del__(self):
        pass

    # Получение активной сессии после запроса из Postgresql
    # def responseCurrentSessionPostgreSQL(self):
    #     try:
    #         self.connection = connect(**self.databaseCheck(), connect_timeout=1)
    #
    #         cursor = self.connection.cursor()
    #         cursor.execute("SELECT pid AS process_id, usename AS username, datname AS database_name,"
    #                        " client_addr AS client_address, application_name, backend_start, state,"
    #                        " state_change FROM pg_stat_activity;")
    #
    #         self.data = cursor.fetchall()
    #
    #         cursor.close()
    #
    #         return self.data
    #
    #     except (Exception, DatabaseError) as ex:
    #         error("[!] [SQL] Error on connectPostgreSQL func >> connection to server, more info : {0}"
    #               .format(ex), exc_info=True)
    #
    #     finally:
    #         if self.connection is not None:
    #             self.connection.close()
    #         else:
    #             pass

    # Подключение к PostgreSQL.
    def connectPostgreSQL(self):
        try:
            self.connection = connect(**self.databaseCheck(), connect_timeout=5)

            cursor = self.connection.cursor()
            cursor.execute(self.get_settings)

            self.data = cursor.fetchall()

            cursor.close()

            return self.data

        except (Exception, DatabaseError) as ex:
            error("[!] [SQL] Error on connectPostgreSQL func >> connection to server, more info : {0}"
                  .format(ex), exc_info=True)

        finally:
            if self.connection is not None:
                # self.responseCurrentSessionPostgreSQL()
                self.connection.close()

                info('\n[+] [SQL] Request : [{0}] completed, connection closed'.format(self.get_settings))
            else:
                pass

    # Подключение к PostgreSQL с перебором всех столбцов дат.
    def editTableWithoutThreads(self, callback_data):
        try:
            self.connection = connect(**self.databaseCheck())

            cursor = self.connection.cursor()
            for time in callback_data:
                cursor.execute("{0} WHERE crnt_date = '{1}'".format(self.get_settings, time[8]))

            self.connection.commit()

        except (Exception, DatabaseError) as ex:
            error("[!] [SQL] Error on editTableWithoutThreads func >> connection to server, more info : {0}"
                  .format(ex), exc_info=True)

        finally:
            if self.connection is not None:
                self.connection.close()

                info('\n[+] [SQL] Request : [{0}] completed, connection closed'.format(self.get_settings))

    # Подключение к PostgreSQL с изменением столбцов по id.
    def editGovWithoutThreads(self, callback_data):
        try:
            self.connection = connect(**self.databaseCheck())

            cursor = self.connection.cursor()
            for id_row in callback_data:
                cursor.execute("{0} WHERE id = '{1}'".format(self.get_settings, id_row))

            self.connection.commit()

        except (Exception, DatabaseError) as ex:
            error("[!] [SQL] Error on editGovWithoutThreads func >> connection to server, more info : {0}"
                  .format(ex), exc_info=True)

        finally:
            if self.connection is not None:
                self.connection.close()

                info('\n[+] [SQL] Request : [{0}] completed, connection closed'.format(self.get_settings))

    # Проверка файла перед соединением.
    def databaseCheck(self):
        self.parser.read(self.filename)

        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            for param in params:
                self.database[param[0]] = param[1]
        else:
            raise Exception('\n[-] File "{0}" not found on "{1}" folder'.format(self.section, self.filename))

        return self.database

    # Проверка соединения со своими параметрами, статичная функция
    @staticmethod
    def testConnectionToPostgreSQL(dbname, user, password, host, port):
        try:
            connection = connect(dbname=dbname, user=user, password=password, host=host, port=port, connect_timeout=5)
            connection.cursor().close()

            return True, str(connection).replace("'", "")

        except (Exception, DatabaseError) as ex:
            error("[!] [SQL] Error on testConnectionToPostgreSQL func >> connection to server, more info : {0}"
                  .format(ex), exc_info=True)

            return False, str(ex).replace("'", "")
