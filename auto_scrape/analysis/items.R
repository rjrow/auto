cwd <- getwd()
source <- file.path(cwd, 'data')

files <- list.files(source)

file.latest <- files[length(files)]


print(file.latest)
print(20)
data <- read.csv(file = file.latest)

write.csv(20, file = "test1.csv")
