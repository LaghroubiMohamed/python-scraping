library(shiny)
library(ggplot2)
library(plyr)
library(dplyr)
library(RSQLite)
library(sqldf)
library(caTools)

setwd("/home/glitcher/Desktop/python scraping")
db <- dbConnect(SQLite(),dbname="base.db" )
dbListTables(db)
dbListFields(db,"coin")


# Importing the dataset
annee <- dbGetQuery(db,"select date,open,high,close,low, ROUND(((low+high)/2),3) as mean from coin where 1=1 group by date order by date") 
deux_mois <- dbGetQuery(db,"select date,open,high,close,low, ROUND(((low+high)/2),3) as mean from coin where 1=1 order by date desc limit 60") 
un_mois <- dbGetQuery(db,"select date,open,high,close,low, ROUND(((low+high)/2),3) as mean from coin where 1=1 order by date desc limit 30")
derniere_semaine <- dbGetQuery(db,"select date,open,high,close,low, ROUND(((low+high)/2),3) as mean from coin where 1=1 and open !=0 order by date desc limit 7") 
dataset <- dbGetQuery(db,"select date,ROUND(((low+high)/2),3) as mean,open,close from coin where 1=1 group by date order by date") 

#NA TRAITMENT
annee <- na.omit(annee)
deux_mois <- na.omit(deux_mois)
un_mois <- na.omit(un_mois)
derniere_semaine <- na.omit(derniere_semaine)
dataset <- na.omit(dataset)

annee$date <- as.Date(annee$date,format= "%Y-%m-%d")#%Y-%m-%d %H:%M:%S
deux_mois$date <- as.Date(deux_mois$date,format= "%Y-%m-%d")
un_mois$date <- as.Date(un_mois$date,format= "%Y-%m-%d")
derniere_semaine$date <- as.Date(derniere_semaine$date,format= "%Y-%m-%d")
dataset$date <- as.Date(dataset$date,format= "%Y-%m-%d")

# Data Split training_set and test_set
split = sample.split(dataset$mean, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Polynomial Regression to the dataset
poly_reg = lm(formula = mean ~ .,
              data = dataset)



#Interactive Visualization with Shiny
ui <- fluidPage(
  # App title
  titlePanel("Shiny - Interactive Visualization Coin Scanner"),
  mainPanel(
    # Output: Histogram
    plotOutput(outputId = "distPlot1"),
    plotOutput(outputId = "distPlot2"),
    plotOutput(outputId = "distPlot3"),
    plotOutput(outputId = "distPlot4"),
    plotOutput(outputId = "distPlot5")
  )
)
# Define server logic required to draw a histogram
server <- function(input, output){
  
  output$distPlot1 <- renderPlot({
    plot (x = annee$date , y = annee$open,xlab = 'Intervale date (Année)' ,ylab = 'Valeur currency' , type = 'l', col='green' , main="Valeurs des actions")
    lines(x= annee$date, y = annee$close ,type = 'l', col='red')
    lines(x= annee$date, y = annee$mean ,type = 'l', col='orange')
    legend("topleft" , title="Line types",legend=c("Valeur open", "Valeur close","Valeur mean"),col=c("green", "red","orange"), lty=1:1, cex=0.7 , bg='lightblue')
    theme(axis.title = element_text(size=12,color="BLACK",face="bold"),
          axis.text = element_text(size=14,color="BLACK",face="bold"))+
      labs(x="Time",y="Black Carbon (ng/m3)",title="Black Carbon Concentration in Air - Dec, 2017",colour="Channel")
    
  })
  
  output$distPlot2 <- renderPlot({
    plot (x = deux_mois$date , y = deux_mois$open,xlab = 'Intervale date (deux mois)' ,ylab = 'Valeur currency' , type = 'l', col='green' , main="Valeurs des actions")
    lines(x= deux_mois$date, y = deux_mois$close ,type = 'l', col='red')
    lines(x= deux_mois$date, y = deux_mois$mean ,type = 'l', col='orange')
    legend("topleft" , title="Line types",legend=c("Valeur open", "Valeur close","Valeur mean"),col=c("green", "red","orange"), lty=1:1, cex=0.7 , bg='lightblue')
    
  })
  
  output$distPlot3 <- renderPlot({
    plot (x = un_mois$date , y = un_mois$open,xlab = 'Intervale date (un mois)' ,ylab = 'Valeur currency' , type = 'l', col='green' , main="Valeurs des actions")
    lines(x= un_mois$date, y = un_mois$close ,type = 'l', col='red')
    lines(x= un_mois$date, y = un_mois$mean ,type = 'l', col='orange')
    legend("topleft" , title="Line types",legend=c("Valeur open", "Valeur close","Valeur mean"),col=c("green", "red","orange"), lty=1:1, cex=0.7 , bg='lightblue')
    
  })
  
  output$distPlot4 <- renderPlot({
    plot (x = derniere_semaine$date , y = derniere_semaine$open,xlab = 'Intervale date (derniere)' ,ylab = 'Valeur currency' , type = 'l', col='green' , main="Valeurs des actions")
    lines(x= derniere_semaine$date, y = derniere_semaine$close ,type = 'l', col='red')
    lines(x= derniere_semaine$date, y = derniere_semaine$mean ,type = 'l', col='orange')
    legend("topleft" , title="Line types",legend=c("Valeur open", "Valeur close","Valeur mean"),col=c("green", "red","orange"), lty=1:1, cex=0.7 , bg='lightblue')
    
  })
  
  output$distPlot5 <- renderPlot({
    ggplot() +
      geom_point(aes(x = dataset$date, y = dataset$mean),
                 colour = 'red') +
      geom_line(aes(x = dataset$date, y = predict(poly_reg, newdata = dataset)),
                colour = 'blue') +
      ggtitle('Polynomial Regression') +
      xlab('Date') +
      ylab('Mean')
    
  })
  
}

shinyApp(ui = ui, server = server)





