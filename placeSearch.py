import googlemaps
import responses
import requests
from __init__ import TestCase
import config
import urllib.request, json

class PlacesSearchTest(TestCase):
    
    def setUp(self, latlong, type, radius):
        self.key = "AIzaSyDJZMEwUkoKPrBqgvF54T9cnwBEqTP4Pzs"
        self.client = googlemaps.Client(self.key)
        self.location = (latlong[0],latlong[1])
        #self.location = (33.696462,-117.798897)
        self.type = type
        #self.type = "restaurant"
        self.language = "en"
        self.region = "US"
        self.radius = radius
        #self.radius = 1000
        
    @responses.activate
    def test_search_places_nearby(self):
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        responses.add(
            responses.GET,
            url,
            body = '{"status": "OK", "results": []}',
            status = 200,
            content_type = "application/json"
        )
        
        self.client.places_nearby(
            location = self.location,
            language = self.language,
            rank_by = "distance",
            type = self.type
            )
        
        # self.assertEqual(1,len(responses.calls))
        # self.assertURLEqual(
        #     "%s?language=en&location=33.696462%%2C-117.798897&rankby=distance&maxprice=None&minprice=None&type=restaurant&key=%s" %(url, self.key),
        #     responses.calls[0].request.url,
        # )
        #print(responses.calls[0].request.url)
        with urllib.request.urlopen(responses.calls[0].request.url) as url:
            config.responseJson = json.loads(url.read().decode())
            #print(config.responseJson)
            
        # with open('current.json', 'w') as output:
        #     json.dump(config.responseJson, output)


# detailTest = PlacesSearchTest()
# detailTest.setUp()
# detailTest.test_search_places_nearby()