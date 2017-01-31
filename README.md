# Python Showcase: League of Legends Real-Time Stat Monitor / Game Analyzer

Hey crew!
This is our team GitHub repo for our Python Showcase Project.

The Game: http://na.leagueoflegends.com/
Riot Developer API: https://developer.riotgames.com/
Django: https://docs.djangoproject.com/en/1.10/intro/overview/

The Python-Backend folder is currently just Python but will need to be ported into a Django project.
The front end will load dynamic content to a web app.

It currently connects up to the Riot API using my Developer Key.
Execute main.py - it re-loads the data from the League servers, exports some data to the command line, and wipes a table in a MySQL database and adds the information into a table on the localhost.

Database information can be found / customized in the insertIntoDB.py file
