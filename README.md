# colonel-cluster
Repository to hold work to support defensive player classification in the NBA.

<img src="http://vignette3.wikia.nocookie.net/dragon-rap-battles/images/2/2d/Colonel_Sanders.png/revision/latest?cb=20151109181735" align="right" />

## Introduction

*From (stats.nba.com)*
Hustle stats evaluate player performances that affect outcomes but cannot be found in traditional box scores. Hustle and activity stats take offensive and defensive analysis to the next level. In addition to standard blocks and steals, players are credited for their defense with contested shots, charges drawn, deflections and loose balls recovered (on offense or defense). On offense, each screen is tracked to examine which players assist in creating scoring opportunities for their teammates.

## Initial Setup
- Clone the project
- Run the setup .sh file
```
sudo ./setup.sh
```
- Create postgresql user and database. The root user will be used as the default owner.
```
sudo su - postgres
createuser root
createdb nba -O root
psql
\password root
password: root
enter it again: root
\q
exit
```

## Data Population

### Non Movement
- Run the db_populate.py script
