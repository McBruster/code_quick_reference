ggplot(DATA, aes(Y_VARIABLE, X_VARIABLE)) + 
	geom_point() +
	xlab("X_LABEL") +
	ylab("Y_LABEL") +
	ggtitle("TITLE") +
	coord_flip()
ggsave("FILE_NAME.png")
