cwd <- getwd()
source <- file.path(cwd, 'data')

files <- list.files(source)


file.latest <- files[length(files)]
mainset <- data.frame()

for(i in 1:length(files))
{
  
  file.pathname <- file.path(source, files[i])
  print(file.pathname)
  tmp_data <- read.csv(file.pathname)

  mainset <- rbind(tmp_data, mainset)

}

