# colonel-cluster
Repository to hold work to support defensive player classification in the NBA.

<img src="http://vignette3.wikia.nocookie.net/dragon-rap-battles/images/2/2d/Colonel_Sanders.png/revision/latest?cb=20151109181735" align="right" />

## Introduction

Following research from my undergraduate year, I continue to pursue accurate lineup recommendation in the NBA. Using past performance data and new evaluation metrics, I hope to achieve a high accuracy in the recommendations and provide an easy understanding in how this research can be applied to the NBA today.

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
