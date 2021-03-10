# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107030016.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
 

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = list(filter(lambda item: item['HUMD'] != '-99.000', data))
target_data = list(filter(lambda item: item['HUMD'] != '-999.000', target_data))
target_station1 = list(filter(lambda item: (item['station_id'] == 'C0A880'), target_data))
target_station2 = list(filter(lambda item: (item['station_id'] == 'C0F9A0'), target_data))
target_station3 = list(filter(lambda item: (item['station_id'] == 'C0G640'), target_data))
target_station4 = list(filter(lambda item: (item['station_id'] == 'C0R190'), target_data))
target_station5 = list(filter(lambda item: (item['station_id'] == 'C0X260'), target_data))


getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]   



#total = sum (map(float,getValues ('HUMD', target_station2)))    

def total(station):
    humd = sum (map(float,getValues ('HUMD', station)))
    if humd == 0:
       return 'NONE' 
    else:
       return humd   

print ([['C0A880', total(target_station1)], ['C0F9A0', total(target_station2)], ['C0G640', total(target_station3)], 
   ['C0R190', total(target_station4)], ['C0X260', total(target_station5)]])  