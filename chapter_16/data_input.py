"""class for generating the csv files ready for table"""
import csv
from pathlib import Path
from datetime import datetime

class Data_input:
    """for using the csv files with"""
    
    def __init__(self, path):
        """aslkdj"""
        self.path = path
        lines = self.path.read_text().splitlines()
        self.lines = lines
    
    def time(self, row_num:int):
        """returns time. requires row number"""
        
        time = []
        reader = csv.reader(self.lines)
        next(reader)
        
        for row in reader:
            current_date = datetime.strptime(row[row_num],'%Y-%m-%d')
            time.append(current_date)
            print(current_date)
        
        return time
       
    def temperature(self,row_num:int):
        """returns temperature. requires the row index for temperature"""
        
        temperature = []
        reader = csv.reader(self.lines)
        next(reader)
        
        for row in reader:
            
            temp = row[row_num]
            if temp.isdigit():
                temp = int(temp)
                
            temperature.append(temp)
              
        return temperature
    
    def index_column(self):
        """"determine the index for columns"""
        reader = csv.reader(self.lines)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)
            
    def station_name(self, row_num:int):
        """determine station name"""
        reader = csv.reader(self.lines)
        next(reader) # skip header
        station_name = next(reader)
        
        return station_name[row_num]
        
    
    
    