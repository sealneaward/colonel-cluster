library(mclust)
# cat("\014")  
if (getwd() == '/home/neil'){
  setwd('projects/colonel-cluster/population')  
}
# read csv and merge
zone_data = read.csv('./data/offense/zone_shooting.csv', header=TRUE)
speed_data = read.csv('./data/speed.csv', header=TRUE)
player_data = read.csv('./data/players.csv', header=TRUE)

data = merge(zone_data, speed_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))
data = merge(data, hustle_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))
data = merge(data, player_data, by=c('PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION'))

# any player that does not average ten or more minutes should be removed
data = data[data$MIN >= 10,]
data = data[data$GP >= 5,]

# subset for columns used in calculations
data = subset(data, select = c(
  'PLAYER_NAME',
  'PLAYER_ID',
  'TEAM_ABBREVIATION',
  'MIN',
  'AVG_SPEED_OFF',
  'PCT_FGA_2PT',
  'PCT_FGA_3PT',
  'PCT_PTS_2PT',
  'PCT_PTS_3PT',
  'PCT_PTS_2PT_MR',
  'PCT_PTS_FB',
  'PCT_PTS_OFF_TOV',
  'PCT_PTS_PAINT',
  'HEIGHT'
  ))

data[mapply(is.infinite, data)] = 0 
data = na.omit(data)

write.csv(data, './data/offense/cluster_metrics.csv', row.names = FALSE, quote = FALSE)

names = data['PLAYER_NAME']
data$PLAYER_NAME = NULL

ids = data['PLAYER_ID']
data$PLAYER_ID = NULL

teams = data['TEAM_ABBREVIATION']
data$TEAM_ABBREVIATION = NULL

data = scale(data)

overall_data = subset(data, select = c(
  'MIN',
  'AVG_SPEED_OFF',
  'PCT_FGA_2PT',
  'PCT_FGA_3PT',
  'PCT_PTS_2PT',
  'PCT_PTS_3PT',
  'PCT_PTS_2PT_MR',
  'PCT_PTS_FB',
  'PCT_PTS_OFF_TOV',
  'PCT_PTS_PAINT',
  'HEIGHT'
))


# overall_model
data = overall_data

BIC = mclustBIC(data)
mod1 = Mclust(data, x = BIC, G=1:10)
print('############################')
print('Overall Model')
print('############################')
summary_clusters = summary(mod1, parameters = TRUE)
distribution_clusters = summary(mod1, parameters = TRUE)$pro
mean_clusters = summary(mod1, parameters = TRUE)$mean
print(summary(mod1, parameters = TRUE))
overall_data = cbind(overall_data, PLAYER_NAME = names)
overall_data = cbind(overall_data, PLAYER_ID = ids)
overall_data = cbind(overall_data, TEAM_ABBREVIATION = teams)
overall_data = cbind(overall_data, CLUSTER = mod1$classification)

png('./plots/overall_cluster_offense.png', width=1800,height=1300,res=300)
mod1dr = MclustDR(mod1, lambda = 1)
plot(mod1dr, what = "scatterplot", xaxt='n', yaxt='n')
title(main="Offense Evaluation Types", col.main="black")
dev.off()

# get cumalitive BIC score
BIC <- rowSums(BIC)/14

png('./plots/overall_cluster_number_offense.png', width=1800,height=1300,res=300)
plot(x=c(1:9),y=BIC,type="l",xlab="Number of Components", ylab="BIC Score")
axis(1, at=1:9)
title(main="BIC Score for Different Offense Cluster Numbers", col.main="black")
dev.off()

png('./plots/distribution_of_clusters_offense.png', width=1800,height=1300,res=300)
x <- overall_data$CLUSTER 
h<-hist(x, breaks=10, col="red", xlab="Offensive Player Classification", 
        main="Distribution of Offensive Classification Types") 
xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="blue", lwd=2)
dev.off()

write.csv(overall_data,file='./data/offense/overall_cluster_offense.csv',row.names=FALSE,quote=FALSE)
write.csv(mean_clusters,file='./data/offense/mean_cluster_offense.csv',row.names=FALSE,quote=FALSE)
