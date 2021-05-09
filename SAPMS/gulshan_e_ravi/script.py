import pandas as pd 
  
# to read csv file named "samplee" 
a = pd.read_csv("gulshan_e_ravi.csv") 
  
# to save as html file 
# named as "Table" 
a.to_html("Table.html") 
  
# assign it to a  
# variable (string) 
html_file = a.to_html()
