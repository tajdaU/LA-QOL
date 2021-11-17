library(ggplot2)
library(dplyr)


#Uploading and Information
la_2y_comparison <-read.csv("C:\\Users\\eduar\\OneDrive - fs-students.de\\02. Intro to Data Analytics\\LA_STORY\\hist_2017_2021.csv")
la_4y_comparison <-read.csv("C:\\Users\\eduar\\OneDrive - fs-students.de\\02. Intro to Data Analytics\\LA_STORY\\hist_2006_2021.csv")

la_2y_comparison <- filter(la_2y_comparison, TotalValue > 0)
la_4y_comparison <- filter(la_4y_comparison, TotalValue > 0)

la_2y_comparison$RollYear <- as.character(la_2y_comparison$RollYear)
la_4y_comparison$RollYear <- as.character(la_4y_comparison$RollYear)


#Median of TotalValue
median_TotalValue_2017 <- median(la_2y_comparison$TotalValue[la_2y_comparison$RollYear=="2017"])
median_TotalValue_2021 <- median(la_2y_comparison$TotalValue[la_2y_comparison$RollYear=="2021"])


#Median of TotalValue
mean_TotalValue_2017 <- mean(la_2y_comparison$TotalValue[la_2y_comparison$RollYear=="2017"])
mean_TotalValue_2021 <- mean(la_2y_comparison$TotalValue[la_2y_comparison$RollYear=="2021"])

mean_TotalValue_2017
mean_TotalValue_2021



#Create a density plot
ggplot(la_2y_comparison, 
       aes(TotalValue, fill = RollYear)) +
  
  labs(
    title = "Density of Properties by Value \nin $USD",
    x = "Property Value ($)",
    y = "Distribution Density",
    fill = "Year") +
  
  xlim(0,2000000)+
  
  geom_density(alpha = 0.2)+
  
  scale_x_continuous(limits = c(0,2000000), 
                     labels = scales::dollar_format()) +
  
  theme(legend.position = "bottom") +

  geom_vline(xintercept=median_TotalValue_2021, size=1, color="lightblue", linetype = "dotted")+
  geom_vline(xintercept=median_TotalValue_2017, size=1, color="lightpink", linetype = "dotted")+
  


