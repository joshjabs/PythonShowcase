class Sum(object):
    def __init__(self, name, level=1, icon= 000, revisionData=000, summonerId=00, botKills=0, champKills=0, minionKills=0,monsterKills=0,turretKills=0,assists=0, wins=0, top=0, mid=0, jg=0, bot=0, champions=[""]):
        self.name = name
        self.level = level
        self.icon = icon
        self.revisionData = revisionData
        self.summonerId = summonerId
        self.botKills = botKills
        self.champKills = champKills
        self.minionKills = minionKills
        self.monsterKills = monsterKills
        self.turretKills = turretKills
        self.assists = assists
        self.wins = wins

        self.top = top
        self.mid = mid
        self.jg = jg
        self.bot = bot

        self.champions = champions

    def __getitem__(self,index):
        return self

    def printName(self):
        print "NAME: " + str(self.name)
    def printLevel(self):
        print "LEVEL: " + str(self.level)
    # def printIcon(self):
    #     print "ICON: " + str(self.icon)
    def printID(self):
        print "ID: " + str(self.summonerId)


    def returnName(self):
        return str(self.name)
    def returnLevel(self):
        return str(self.level)
    def returnIcon(self):
        return str(self.icon)
    def returnID(self):
        return str(self.summonerId)
    def returnBotKills(self):
        return str(self.botKills)
    def returnChampKills(self):
        return str(self.champKills)

    def returnMinionKills(self):
        return str(self.minionKills)
    def returnMonsterKills(self):
        return str(self.monsterKills)
    def returnTurretKills(self):
        return str(self.turretKills)
    def returnAssists(self):
        return str(self.assists)

    def returnWins(self):
        if self.wins < 4:
            return "COLD"
        if self.wins > 6:
            return "HOT"
        else:
            return "50/50"

    def returnTOP(self):
        return str(self.top) + "/10"
    def returnMID(self):
        return str(self.mid) + "/10"
    def returnJG(self):
        return str(self.jg) + "/10"
    def returnBOT(self):
        print str(self.bot) + "/10"

    def returnFavLane(self):
        if self.top >4:
            return "Top"
        elif self.mid >4:
            return "Mid"
        elif self.jg >4:
            return "Jungle"
        elif self.bot >4:
            return "Bot"
        else:
            return "None"

    def returnRecentChamp(self):
        string = ""
        for self.champion in self.champions:
            string += self.champion + " "
        return string


    def returnCurrentChamp(self):
        url = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/" + str(self.summonerId) + "?api_key=" + API_KEY
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        for idx, obj in enumerate(data['participants']):
            print data['participants'][idx]['summonerName']
            if(data['participants'][idx]['summonerName'] == self.summonerId):
                print data['participants'][idx]['championId'] + "TEST"
                return data['participants'][idx]['championId']
