library(tm)
cwd <- getwd()

data.path <- file.path(cwd, "auto_scrape", "items.csv")
analysis.path <-  file.path(cwd, "auto_scrape", "analysis","data")

#data <- read.csv(data.path)

###############################################################################################################
# Munge the description, which will need to be cleaned and then piped into a new process for mining

dcp <- data$description

dcp.v1 <- gsub("\n        ", "", dcp)
dcp.v2 <- gsub("\n", "", dcp.v1)

corpus <- Corpus(VectorSource(dcp.v2))
corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removeWords, stopwords("english"))


for(i in 1:length(10000))
{
  setwd(analysis.path)
  x <- corpus[[i]]
  filename <- paste0("corpus_",i)
  write(x, filename)
}




setwd(cwd)
