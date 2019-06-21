# install.packages("rvest")
library(rvest)
getwd()

url_base = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=167099&target=after&page="
all.review <-c()
for(page in 1:20){
  url <- paste(url_base, page, sep='', Encoding="euc_kr")
  htxt <- read_html(url)
  table <- html_nodes(htxt, ".list_netizen")
  content <- html_nodes(table, ".title")
  reviews <- html_text(content)
  if(length(reviews) == 0){break}
  all.review <- c(all.review, reviews)
  print(page)
}

all.review
