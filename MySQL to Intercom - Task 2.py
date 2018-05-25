

from mysql.connector import errorcode
from intercom.client import Client



class IntercomUser():
    """
    Using MySQL database to create Intercom users. Users have following properties:

    Attributes:
        id: Auto-incremented integer up to 11 digits long.
        name: A string representing the user's name.
        email: A string up to 120 characters long representing the user's email.
    """

    def __init__(self):

        # Connect to Intercom API
        self.intercom = Client(personal_access_token='personal_access_token')

        # Connect to the database
        try:
            self.cnx = mysql.connector.connect()

        except


        # Get all users from MySQL table


    def create_Intercom_user(self):

        # Go through each table user entry, call API
        for id, name, email in ## table
            self.intercom.users.create(user_id = id,
                                       email=email,
                                       name=name)

    def stop(self):

        # Shut down




if __name__ == '__main__':


