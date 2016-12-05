library(mclust)
# cat("\014")  
if (getwd() == '/home/neil'){
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
  'TEAM_ABBREVIATION',
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
# Make time factor to normalize to per 40  min for each metric
########################################
data = transform(data, TIME_NORMAL = 40 / MIN)


########################################
# Make products of volume and percentage, then segment skills to three zones: paint, mid range, and three
########################################
# data = transform(data, OPP_FGA_RA = (OPP_FGA_RA*TIME_NORMAL) / OPP_FG_PCT_RA)
# data = transform(data, OPP_NRA = (OPP_FGA_NRA*TIME_NORMAL) / OPP_FG_PCT_NRA)
# data = transform(data, OPP_MR = (OPP_FGA_MR*TIME_NORMAL) / OPP_FG_PCT_MR)
# data = transform(data, OPP_LC3 = (OPP_FGA_LC3*TIME_NORMAL) / OPP_FG_PCT_LC3)
# data = transform(data, OPP_RC3 = (OPP_FGA_RC3*TIME_NORMAL) / OPP_FG_PCT_RC3)
# data = transform(data, OPP_AB3 = (OPP_FGA_AB3*TIME_NORMAL) / OPP_FG_PCT_AB3)

data = transform(data, OPP_FGA_RA = OPP_FGA_RA*TIME_NORMAL)
data = transform(data, OPP_NRA = OPP_FGA_NRA*TIME_NORMAL)
data = transform(data, OPP_MR = OPP_FGA_MR*TIME_NORMAL)
data = transform(data, OPP_LC3 = OPP_FGA_LC3*TIME_NORMAL)
data = transform(data, OPP_RC3 = OPP_FGA_RC3*TIME_NORMAL)
data = transform(data, OPP_AB3 = OPP_FGA_AB3*TIME_NORMAL)

data = transform(data, CONTESTED_SHOTS_2PT = (CONTESTED_SHOTS_2PT*TIME_NORMAL)/(OPP_FGA_RA + OPP_FGA_NRA + OPP_MR))
data = transform(data, CONTESTED_SHOTS_3PT = (CONTESTED_SHOTS_3PT*TIME_NORMAL)/(OPP_LC3 + OPP_RC3 + OPP_AB3))
data = transform(data, DEFLECTIONS = DEFLECTIONS*TIME_NORMAL)
data = transform(data, DREB = DREB*TIME_NORMAL)
data = transform(data, STL = STL*TIME_NORMAL)
data = transform(data, BLK = BLK*TIME_NORMAL)
data = transform(data, BLK_PER_SHOT = BLK/(OPP_FGA_RA + OPP_FGA_NRA + OPP_MR + OPP_LC3 + OPP_RC3 + OPP_AB3))
data = transform(data, LOOSE_BALLS_RECOVERED = LOOSE_BALLS_RECOVERED*TIME_NORMAL)

data = transform(data, OPP_PAINT = (OPP_NRA + OPP_NRA)/2)
data = transform(data, OPP_CORNER_THREE = (OPP_LC3 + OPP_RC3)/2)
data = transform(data, OPP_ABOVE_KEY = OPP_AB3)
data = transform(data, OPP_MR = (OPP_MR + OPP_NRA)/2)


data = subset(data, select = c(
  'PLAYER_NAME',
  'TEAM_ABBREVIATION',
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'DEFLECTIONS',
  'BLK_PER_SHOT',
  'DREB',
  'STL',
  'BLK',
  'LOOSE_BALLS_RECOVERED',
  'AVG_SPEED_DEF'
))

data[mapply(is.infinite, data)] = 0 
data = na.omit(data)

write.csv(data, './data/cluster_metrics.csv', row.names = FALSE, quote = FALSE)

names = data['PLAYER_NAME']
data$PLAYER_NAME = NULL

teams = data['TEAM_ABBREVIATION']
data$TEAM_ABBREVIATION = NULL

data = scale(data)

# # create frames of related stats
# zone_data = subset(data, select = c(
#   'OPP_RA',
#   'OPP_NRA',
#   'OPP_MR',
#   'OPP_LC3',
#   'OPP_RC3',
#   'OPP_AB3'
# ))

contested_data = subset(data, select = c(
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'BLK_PER_SHOT'
))

handle_data = subset(data, select = c(
  'DEFLECTIONS',
  'STL',
  'BLK',
  'LOOSE_BALLS_RECOVERED',
  'DREB',
  'AVG_SPEED_DEF'
))

overall_data = subset(data, select = c(
  'CONTESTED_SHOTS_2PT',
  'CONTESTED_SHOTS_3PT',
  'BLK_PER_SHOT',
  'DEFLECTIONS',
  'STL',
  'LOOSE_BALLS_RECOVERED',
  'DREB',
  'AVG_SPEED_DEF'
))


# overall_model
data = overall_data

BIC = mclustBIC(data)
mod1 = Mclust(data, x = BIC)
print('############################')
print('Overall Model')
print('############################')
print(summary(mod1, parameters = TRUE))
overall_data = cbind(overall_data, PLAYER_NAME = names)
overall_data = cbind(overall_data, TEAM_ABBREVIATION = teams)
overall_data = cbind(overall_data, CLUSTER = mod1$classification)

png('./plots/overall_cluster.png', width=1800,height=1000,res=300)
mod1dr = MclustDR(mod1, lambda = 1)
plot(mod1dr, what = "scatterplot")
title(main="Defense Evaluation Types", col.main="black")
dev.off()

png('./plots/overall_cluster_number.png', width=1800,height=1000,res=300)
plot(BIC)
title(main="BIC Score for Different Cluster Numbers", col.main="black")
dev.off()

write.csv(overall_data,file='./data/overall_cluster.csv',row.names=FALSE,quote=FALSE)
# 
# # contest_model
# data = contested_data
# 
# BIC = mclustBIC(data)
# mod1 = Mclust(data, x = BIC)
# print('############################')
# print('Contest Model')
# print('############################')
# print(summary(mod1, parameters = TRUE))
# contested_data = cbind(contested_data, PLAYER_NAME = names)
# contested_data = cbind(contested_data, CLUSTER = mod1$classification)
# 
# png('./plots/contest_cluster.png', width=1400,height=1100,res=300)
# mod1dr = MclustDR(mod1, lambda = 1)
# plot(BIC)
# title(main="Contesting Defense Evaluation Types", col.main="black")
# dev.off()
# 
# write.csv(contested_data,file='./data/contest_cluster.csv',row.names=FALSE,quote=FALSE)    
# 
# # handle_model
# data = handle_data
# 
# BIC = mclustBIC(data)
# mod1 = Mclust(data, x = BIC)
# print('############################')
# print('Handle Model')
# print('############################')
# print(summary(mod1, parameters = TRUE))
# handle_data = cbind(handle_data, PLAYER_NAME = names)
# handle_data = cbind(handle_data, CLUSTER = mod1$classification)
# 
# png('./plots/handle_cluster.png', width=1400,height=1200,res=300)
# mod1dr = MclustDR(mod1, lambda = 1)
# plot(BIC)
# title(main="Ball Handle Defense Evaluation Types", col.main="black")
# dev.off()
# 
# write.csv(handle_data,file='./data/handle_cluster.csv',row.names=FALSE,quote=FALSE)
