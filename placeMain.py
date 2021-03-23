from placeSearch import PlacesSearchTest
from placeDetail import PlacesDetailTest
import config
import json
import csv
import os

def main():
    config.responseJson = {}
    config.detailsJson = {}
    latlonglist = input("Input 2 comma separated values for latitude and longitude: \n")
    list = latlonglist.split(",")
    latlong = tuple(list)
    type = input("Input type of business: \n")
    radius = input("Input radius from the lat and long: \n")
    currentArea = PlacesSearchTest()
    currentArea.setUp(latlong, type, radius)
    currentArea.test_search_places_nearby()
    totexamples = []
    for item in config.responseJson["results"]:
        detailexample = PlacesDetailTest()
        detailexample.setUp(item["place_id"])
        detailexample.test_get_info()
        totexamples.append(config.detailsJson)
    
    for item in totexamples:
        del item['html_attributions']
        del item['status']
        
    try:
        keys = totexamples[0]['result'].keys()
        
        with open('unordereddetailsfile.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            for item in totexamples:
                try:
                    dict_writer.writerow(item['result'])
                except UnicodeEncodeError:
                    pass
            
            
        with open('unordereddetailsfile.csv','r') as input_file, open('detailsfile.csv','w') as output_file:
            fields = ['name','formatted_address','formatted_phone_number','website']
            writer = csv.DictWriter(output_file, fieldnames=fields)
            writer.writeheader()
            for row in csv.DictReader(input_file):
                writer.writerow(row)
                
        os.remove('unordereddetailsfile.csv')
    
    except IndexError:
        pass
    
if __name__ == "__main__":
    main() 