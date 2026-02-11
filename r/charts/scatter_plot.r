#One dimensional scatterplot
ggplot(hof, aes(x=VARIABLE, y=1)) +
    geom_jitter(height= 0.6) + ylim(-1,3) +
    theme(axis.title.y= element_blank(),
	axis.text.y= element_blank(),
	axis.ticks.y= element_blank())+
 coord_fixed(ratio=0.03)