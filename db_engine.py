"""
This application uses postgresql database.
You have to set_up your credentials here
"""


username = ""
password = ""
port = ""
db_name = ""   # make sure database exists

db_url = f"postgresql://{username}:{password}@{port}/{db_name}"