import urllib, json, os, sys
# Add the directory containing our custom modules to the Python path (wants absolute paths)
scriptpath = "../Summoner.py"
sys.path.append(os.path.abspath(scriptpath))
from SummonerClass import Sum

# Add the directory containing our custom modules to the Python path (wants absolute paths)
scriptpath = "../insertIntoDB.py"
sys.path.append(os.path.abspath(scriptpath))
from insertIntoDB import DB_CON_OPEN, DB_CON_CLOSE, DB_INSERT

DB_CON_OPEN()


API_KEY = "RGAPI-78763f39-c513-445f-8b80-ed996e26d74e"
Summoners = ['CopperMatrix', 'RoyInvincible', 'FierceAtalanta']
# MY_USER_ID = 73733149
# url = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/" + str(MY_USER_ID) + "?api_key=" + API_KEY
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# for idx, obj in enumerate(data['participants']):
#     Summoners.append(data['participants'][idx]['summonerName'])

SummonerObjects = []
query = ""

for idx, Summoner in enumerate(Summoners):
    query += (Summoners[idx] + ',%20')

url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + query + "?api_key=" + API_KEY
response = urllib.urlopen(url)
data = json.loads(response.read())

for majorkey, subdict in data.iteritems():
    name = (data[majorkey]['name'])
    level = (data[majorkey]['summonerLevel'])
    icon = (data[majorkey]['profileIconId'])
    revisionData = (data[majorkey]['revisionDate'])
    summonerId = (data[majorkey]['id'])


#Return Total Stats
    botKills = 0
    champKills = 0
    minionKills = 0
    monsterKills = 0
    turretKills = 0
    assists = 0

    StatsURL = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/" + str(summonerId) + "/summary?season=SEASON2016" "&api_key=" + API_KEY
    response2 = urllib.urlopen(StatsURL)
    Statsdata = json.loads(response2.read())
    for idx, obj in enumerate(Statsdata['playerStatSummaries']):
        if("Coop" in str(Statsdata['playerStatSummaries'][idx]['playerStatSummaryType'])):
            if('totalChampionKills' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
                botKills += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalChampionKills'])
        else:
            if('totalChampionKills' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
                champKills += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalChampionKills'])

        if('totalMinionKills' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
            minionKills += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalMinionKills'])
        if('totalTurretsKilled' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
            turretKills += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalTurretsKilled'])
        if('totalNeutralMinionsKilled' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
            monsterKills += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalNeutralMinionsKilled'])
        if('totalAssists' in Statsdata['playerStatSummaries'][idx]['aggregatedStats']):
            assists += (Statsdata['playerStatSummaries'][idx]['aggregatedStats']['totalAssists'])

#Return Recent Game Stats
    wins = 0
    top = 0
    mid = 0
    jg = 0
    bot = 0
    champions = []


    StatsURL = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(summonerId) + "/recent?api_key=" + API_KEY
    response3 = urllib.urlopen(StatsURL)
    Statsdata = json.loads(response3.read())
    for idx, obj in enumerate(Statsdata['games']):
        #Win Streak
        if(Statsdata['games'][idx]['stats']['win']):
            wins+=1

        #Player position (Legal values: TOP(1), MIDDLE(2), JUNGLE(3), BOT(4))
        if('playerPosition' in Statsdata['games'][idx]['stats']):
            if(Statsdata['games'][idx]['stats']['playerPosition'] is 1):
                top+=1
            if(Statsdata['games'][idx]['stats']['playerPosition'] is 2):
                mid+=1
            if(Statsdata['games'][idx]['stats']['playerPosition'] is 3):
                jg+=1
            if(Statsdata['games'][idx]['stats']['playerPosition'] is 4):
                bot+=1


            ChampURL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(Statsdata['games'][idx]['championId']) + "?api_key=" + API_KEY
            responseChamp = urllib.urlopen(ChampURL)
            Champdata = json.loads(responseChamp.read())
            ChampName = Champdata['name']

            if(ChampName not in champions):
                champions.append(ChampName)


    newSummoner = Sum(name, level, icon, revisionData, summonerId, botKills, champKills, minionKills,monsterKills,turretKills,assists, wins, top, mid, jg, bot, champions)
    SummonerObjects.append(newSummoner)

#Prints all Local Summoner Objects
for idx, SummonerObject in enumerate(SummonerObjects):
    SummonerObject[idx].printName()
    SummonerObject[idx].printLevel()
    # SummonerObject[idx].printBotKills()
    # SummonerObject[idx].printChampKills()
    # SummonerObject[idx].printMinionKills()
    # SummonerObject[idx].printMonsterKills()
    # SummonerObject[idx].printTurretKills()
    # SummonerObject[idx].printAssists()
    #
    # SummonerObject[idx].printIcon()
    SummonerObject[idx].printID()
    # SummonerObject[idx].printWins()

    # SummonerObject[idx].printTOP()
    # SummonerObject[idx].printMID()
    # SummonerObject[idx].printJG()
    # SummonerObject[idx].printBOT()

    # SummonerObject[idx].printFavLane()
    # SummonerObject[idx].printRecentChamp()
    DB_INSERT(SummonerObject)



    print "\n"


DB_CON_CLOSE()
