import mysql.connector
from mysql.connector import errorcode
from intercom.client import Client



class IntercomUser:
    """
    Using MySQL database to create Intercom users. Users have the following properties:

    Attributes:
        id: Auto-incremented integer up to 11 digits long
        name: A string representing the user's name
        email: A string up to 120 characters long representing the user's email
    """

    def __init__(self, personal_access_token, user, password, host, database):

        self.personal_access_token = personal_access_token
        self.user = user
        self.password = password
        self.host = host
        self.database = database


    def connect_to_Intercom(self):

        self.intercom = Client(personal_access_token = self.personal_access_token)

        try:
            pass


    def connect_to_database(self):
        try:
            self.cnx = mysql.connector.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               database=self.database)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied: Invalid username or password.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            else:
                print(err)


    def data_from_MySQL(self):
        self.cursor = self.cnx.cursor()

        # Get all users from MySQL table
        query = "SELECT id, name, email FROM user"
        self.cursor.execute(query)


    def create_Intercom_user(self):

        # Go through each MySQL table user entry, creates Intercom user
        for id, name, email in self.cursor:
            self.intercom.users.create(user_id=id,
                                       email=email,
                                       name=name)


    def stop(self):
        self.cursor.close()
        self.cnx.close()


    def run(self):
        self.connect_to_Intercom()
        self.connect_to_database()
        self.data_from_MySQL()
        self.create_Intercom_user()
        self.stop()


if __name__ == '__main__':
    user_transfer = IntercomUser(personal_access_token="token", user="user",
                                 password="password", host="127.0.0.1", database="Monument")
    user_transfer.run()
