import os
import mysql.connector as MS

main_configs = {
    'user' : os.getenv("CUSER"),
    'password' : os.getenv("CPWD"),
    'host' : os.getenv("CHOST"),
    'database' : os.getenv("CDBNAME")
}

db = MS.connect(user=main_configs['user'],
    password=main_configs['password'],
    host=main_configs['host'],
    database=main_configs['database'],
    use_pure=False
)


