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
## Data Population
- Navigate to the population folder in the project

- Populate the data

```
python populate.py
```

- Perform clustering

```
Rscript clustering.py
```

- Run team by team analysis

```
python clustering_analysis.py
```
