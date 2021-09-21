### Cohort table
# setwd("~/Desktop/GonJoy/Right Time/")
#
# Table_Cohort <-read_csv("Table_Cohort_2.csv")
# Table_Cohort <- Table_Cohort[,-1]
#
# Table_Cohort_1 <- Table_Cohort[order(Table_Cohort$Var2, decreasing = T),]
# Table_Cohort_Full <- dcast(Table_Cohort_1, Var1 ~ Var2, value.var="Freq")
#
# Table_Cohort_Full_order <- Table_Cohort_Full[,c(1,ncol(Table_Cohort_Full):2)]
#
#
# for (i in 1:dim(Table_Cohort_Full_order)[1]) {
#
# Table_Cohort_Full_order[i,1:(ncol(Table_Cohort_Full_order)-i+1)] <- Table_Cohort_Full_order[i,c(1,(ncol(Table_Cohort_Full_order)-i+1):(2))]
#
# }
#
# names(Table_Cohort_Full_order)
#
# write.csv(Table_Cohort_Full_order,"Retention_Cohort_2.csv")
#
# Table_Cohort_cal <- read_csv("Retention_Cohort_2.csv")
#
# Table_Cohort_cal <- Table_Cohort_cal[,-1]

import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from operator import attrgetter
import matplotlib.colors as mcolors

# df = pd.read_excel('Online Retail.xlsx',
#                    dtype={'CustomerID': str,
#                           'InvoiceID': str},
#                    parse_dates=['InvoiceDate'],
#                    infer_datetime_format=True)

# https://towardsdatascience.com/a-step-by-step-introduction-to-cohort-analysis-in-python-a2cbbd8460ea