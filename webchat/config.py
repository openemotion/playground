import os

if os.getenv("MODE") == "production":
    DATABASE = "/home/dotcloud/current/data.db"
    SECRET_KEY = "8DC1DE50136CA4F4217E928893CA4866"
else:
    DATABASE = "data.db"
    SECRET_KEY = "development key"
