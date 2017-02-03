data <- as.data.frame(read.csv('Documents/Data/Focus Area - Image Processing/data.csv',stringsAsFactors = F))
beerCategory_unique <- unique(data[,c(2,3)])
week_unique <- unique(data[,c(1)])

# z <- list()
# a <- mapply(function (x,y){
#    z[x] <- cbind( z[x], subset(data, Brand==x & SKU==y)[,4])
# }, beerCategory_unique$Brand, beerCategory_unique$SKU )

# subset(data, Brand=='BROOKLYN INDIA PALE' & SKU=='6 Pk 12 Oz Glass')


write.csv(as.data.frame(beerCategory_unique),"ROI.csv")