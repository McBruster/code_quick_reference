#regular bar chart
ggplot(DATA, aes(x=VARIABLE)) + 
	geom_bar() +
	xlab("X_LABEL") +
	ylab("Y_LABVEL") +
	ggtitle("TITLE")
ggsave("FILE_NAME.png")


#histogram with specified bins
ggplot(DATA, aes(x=VARIABLE)) + 
	geom_histogram(breaks = seq(0.4, 1.2, by =0.1),
	color= "blue", fill="white")
ggsave("FILE_NAME.png")