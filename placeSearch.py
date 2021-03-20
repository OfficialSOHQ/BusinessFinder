import googlemaps
import uuid
from types import GeneratorType
import responses
from __init__ import TestCase


class PlacesTest(TestCase):
    def setUp(self):
        self.key = "AIzaSyDJZMEwUkoKPrBqgvF54T9cnwBEqTP4Pzs"
        self.client = googlemaps.Client(self.key)
        self.location = (33.696462, -117.798897)
        self.type = "restaurant"
        self.language = "en"
        self.region = "US"
        self.radius = 1000
        
    @responses.activate
    def test_search_places_nearby(self):
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        responses.add(
            responses.GET,
            url,
            body = '{"status": "OK", "results": [], "html_attributions":[]}',
            status = 200,
            content_type = "application/json"
        )
        
        self.client.places_nearby(
            location = self.location,
            language = self.language,
            rank_by = "distance",
            type = self.type
            )
        
        self.assertEqual(1,len(responses.calls))
        self.assertURLEqual(
            "%s?language=en&location=33.696462%%2C-117.798897&rankby=distance&maxprice=None&minprice=None&type=restaurant&key=%s" %(url, self.key),
            responses.calls[0].request.url,
        )
        print(responses.calls[0].request.url)
        

t1 = PlacesTest()
t1.setUp()
t1.test_search_places_nearby()
