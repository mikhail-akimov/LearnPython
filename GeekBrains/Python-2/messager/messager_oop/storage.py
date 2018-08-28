from chat import Chat
import sqlite3
import sqlalchemy


class Storage(Chat):
    def __init__(self, config):
        super().__init__(config)
        self.cursor = sqlite3.connect('messager.db3').cursor()

    def create_new(self):
        self.cursor.execute("""
                        create table if not exists Client (
                            id  INTEGER primary key, 
                            login TEXT, 
                            information TEXT
                        );
            """)

        self.cursor.execute("""
                        create table if not exists Client_history (
                            login_time datetime, 
                            login TEXT, 
                            ip_address TEXT
                        );
            """)

        self.cursor.execute("""
                        create table if not exists ContactList (
                            owner_id INTEGER,
                            client_id INTEGER
                        );
            """)

    def add_event(self):
        pass


class ContactList(Storage):

    def add_contact(self, owner, contact):
        self.cursor.execute("""
                    insert into ContactList (owner_id, client_id)
                    VALUES (?, ?);""",
                            (owner, contact)
                            )

    def del_contact(self, owner, contact):
        self.cursor.execute("""
                            delete from ContactList (owner_id, client_id)
                            VALUES (?, ?);""",
                            (owner, contact)
                            )

    def get_contact_list(self, owner):
        return self.cursor.execute('select * from ContactList where owner_id =?', owner)

# Storage.create_new(Storage)

#still not working
