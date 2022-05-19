library(ggplot2)
library(reshape2)
df <- escuelas

ggplot2:: ggplot(df) +
  geom_point(aes(x=df$School, y=["df$`2020-2019`",df$`2019-2018`]))

