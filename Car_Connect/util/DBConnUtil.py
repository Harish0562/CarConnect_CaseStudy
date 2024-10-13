import pyodbc


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OFHDUG6;'
                      'Database=casestudy_db;'
                      'Trusted_Connection=yes;')

            return connection
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None