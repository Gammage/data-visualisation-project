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


    
    def time(self):
        """returns time"""
        
        time = []
        reader = csv.reader(self.lines)
        next(reader)
        
        for row in reader:
            current_date = datetime.strptime(row[0],'%Y%m')
            time.append(current_date)
            print(current_date)
        
        return time
       
    def temperature(self):
        """returns temperature"""
        
        temperature = []
        reader = csv.reader(self.lines)
        next(reader)
        
        for row in reader:
            temp = float(row[1])
            temperature.append(temp)
             
        return temperature
        
