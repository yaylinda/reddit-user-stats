setwd("~/Developer/reddit-user-stats")

library(ggplot2)

data = read.csv('data.csv')

data$time = as.POSIXct(as.numeric(data$created_utc), origin = "1970-01-01", tz = "CDT")

data = data[order(data$time),]


ggplot(data, aes(x = data$time, y = cumsum(data$score))) + 
  geom_point(aes(color = data$type))
