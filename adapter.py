import time
import json
import libsql_experimental as libsql
import settings

conn = libsql.connect(database=settings.turso_db_url,
                      auth_token=settings.turso_db_token)

def reconnect():
   global conn
   conn = libsql.connect(database=settings.turso_db_url,
                      auth_token=settings.turso_db_token)

def get_settings():
   notcorrect = conn.execute("select * from settings").fetchall()
   temp = {}
   for i in notcorrect:
      temp[i[0]] = i[1]
   return temp

def get_stat():
   notcorrect = conn.execute("select * from history").fetchall()
   temp = {}
   for i in notcorrect:
      temp[i[0]] = i[1]
   return temp

def set_stat(feat, value):
   conn.execute("INSERT OR REPLACE INTO history (feature, usage) VALUES ('" + feat + "','" + value + "');")
