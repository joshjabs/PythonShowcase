import MySQLdb, os, sys
# Add the directory containing our custom modules to the Python path (wants absolute paths)
scriptpath = "../SummonerClass.py"
sys.path.append(os.path.abspath(scriptpath))
from SummonerClass import Sum

db = MySQLdb.connect(host= "localhost",
                      user="root",
                      passwd="root",
                      db="LOL")
cursor = db.cursor()



def DB_CON_OPEN():
    x = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS team")
    sql = """CREATE TABLE team (NAME VARCHAR(30),  LEVEL INT, ID INT, STREAK VARCHAR(50), FAV_LANE VARCHAR(20), RECENT_CHAMPS VARCHAR(250), BOT_KILLS INT, CHAMP_KILLS INT)"""
    cursor.execute(sql)



def DB_INSERT(Sum):
    try:
        cursor.execute("""INSERT INTO team VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(Sum.returnName(),Sum.returnLevel(),
        Sum.returnID(), Sum.returnWins(), Sum.returnFavLane(), Sum.returnRecentChamp(), Sum.returnBotKills(), Sum.returnChampKills()))
        db.commit()
    except:
        db.rollback()
        print("ERROR IN UPDATING DATABASE")

def DB_CON_CLOSE():
    db.close()
