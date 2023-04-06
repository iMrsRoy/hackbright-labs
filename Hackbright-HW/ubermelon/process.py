# this opens the file 
log_file = open("um-server-01.txt") 

#this is a sales report functions
def generate_sales_reports(log_file):
    for line in log_file: #this reads all the lines in the log_file
        line = line.rstrip() #method removes extra white space to right
        day = line[0:2] #index the name of the day
        if day == "Mo": # if condition matches 
            print(line) # print the line