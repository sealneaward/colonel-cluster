library(mclust)
# cat("\014")  
if (getwd() == '/home/neil/'){
  setwd('projects/colonel-cluster/population')  
}
# read csv and merge
zone_data = read.csv('./data/zone_shooting.csv', header=TRUE)
speed_data = read.csv('./data/speed.csv', header=TRUE)
hustle_data = read.csv('./data/hustle.csv', header=TRUE)
overall_data = read.csv('./data/overall_defense.csv', header=TRUE)

data = merge(zone_data, speed_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))
data = merge(data, hustle_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))
data = merge(data, overall_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))

# any player that does not average ten or more minutes should be removed
data = data[data$MIN >= 10,]

# subset for columns used in calculations
data = subset(data, select = c(
  'PLAYER_NAME',
  'MIN',
  'AVG_SPEED_OFF',
  'AVG_SPEED_DEF',
  'BLK',
  'CONTESTED_SHOTS',
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'DEFLECTIONS',
  'DREB',
  'LOOSE_BALLS_RECOVERED',
  'OPP_FGA_RA',
  'OPP_FG_PCT_RA',
  'OPP_FGA_NRA',
  'OPP_FG_PCT_NRA',
  'OPP_FGA_MR',
  'OPP_FG_PCT_MR',
  'OPP_FGA_LC3',
  'OPP_FG_PCT_LC3',
  'OPP_FGA_RC3',
  'OPP_FG_PCT_RC3',
  'OPP_FGA_AB3',
  'OPP_FG_PCT_AB3',
  'STL'
  ))

########################################
# Make products of volume and percentage, then segment skills to three zones: paint, mid range, and three
########################################
data = transform(data, OPP_RA = OPP_FGA_RA / OPP_FG_PCT_RA)
data = transform(data, OPP_NRA = OPP_FGA_NRA / OPP_FG_PCT_NRA)
data = transform(data, OPP_MR = OPP_FGA_MR / OPP_FG_PCT_MR)
data = transform(data, OPP_LC3 = OPP_FGA_LC3 / OPP_FG_PCT_LC3)
data = transform(data, OPP_RC3 = OPP_FGA_RC3 / OPP_FG_PCT_RC3)
data = transform(data, OPP_AB3 = OPP_FGA_AB3 / OPP_FG_PCT_AB3)

data = transform(data, OPP_PAINT = (OPP_NRA + OPP_NRA)/2)
data = transform(data, OPP_THREE = (OPP_LC3 + OPP_RC3 + OPP_AB3)/3)
data = transform(data, SPEED_DIFF = (AVG_SPEED_DEF - AVG_SPEED_OFF))


data = subset(data, select = c(
  'PLAYER_NAME',
  'OPP_PAINT',
  'OPP_MR',
  'OPP_THREE',
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'DEFLECTIONS',
  'DREB',
  'STL',
  'BLK',
  'LOOSE_BALLS_RECOVERED',
  'SPEED_DIFF'
))

data[mapply(is.infinite, data)] = 0 
data = na.omit(data)

write.csv(data, './data/cluster_metrics.csv', row.names = FALSE, quote = FALSE)

names = data['PLAYER_NAME']
data$PLAYER_NAME = NULL

data = scale(data)

# create frames of related stats
zone_data = subset(data, select = c(
  'OPP_PAINT',
  'OPP_MR',
  'OPP_THREE',
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'DREB'
))

contested_data = subset(data, select = c(
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'DEFLECTIONS',
  'BLK'
))

handle_data = subset(data, select = c(
  'DEFLECTIONS',
  'STL',
  'BLK',
  'LOOSE_BALLS_RECOVERED',
  'DREB'
))

# zone_model
data = zone_data

BIC = mclustBIC(data)
mod1 = Mclust(data, x = BIC)
print(summary(mod1, parameters = TRUE))
zone_data = cbind(zone_data, PLAYER_NAME = names)
zone_data = cbind(zone_data, CLUSTER = mod1$classification)

jpeg('./plots/zone_cluster.jpg')
mod1dr = MclustDR(mod1, lambda = 1)
plot(mod1dr, what = "scatterplot")
dev.off()

write.csv(zone_data,file='./data/zone_cluster.csv',row.names=FALSE,quote=FALSE)    

# contest_model
data = contested_data

BIC = mclustBIC(data)
mod1 = Mclust(data, x = BIC)
print(summary(mod1, parameters = TRUE))
contested_data = cbind(contested_data, PLAYER_NAME = names)
contested_data = cbind(contested_data, CLUSTER = mod1$classification)

jpeg('./plots/contest_cluster.jpg')
mod1dr = MclustDR(mod1, lambda = 1)
plot(mod1dr, what = "scatterplot")
dev.off()

write.csv(contested_data,file='./data/contest_cluster.csv',row.names=FALSE,quote=FALSE)    

# handle_model
data = handle_data

BIC = mclustBIC(data)
mod1 = Mclust(data, x = BIC)
print(summary(mod1, parameters = TRUE))
handle_data = cbind(handle_data, PLAYER_NAME = names)
handle_data = cbind(handle_data, CLUSTER = mod1$classification)

jpeg('./plots/handle_cluster.jpg')
mod1dr = MclustDR(mod1, lambda = 1)
plot(mod1dr, what = "scatterplot")
dev.off()

write.csv(handle_data,file='./data/handle_cluster.csv',row.names=FALSE,quote=FALSE)    
