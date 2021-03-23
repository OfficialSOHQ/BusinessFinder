import googlemaps
import responses
import requests
from __init__ import TestCase
import config
import urllib.request, json

class PlacesDetailTest(TestCase):
    
    def setUp(self, id):
        self.key = #***INSERT API KEY HERE***
        self.client = googlemaps.Client(self.key)
        self.id = id
        self.language = "en"
    
    @responses.activate
    def test_get_info(self):
        url = "https://maps.googleapis.com/maps/api/place/details/json"
        responses.add(
            responses.GET,
            url,
            body='{"status": "OK", "result": {}}',
            status=200,
            content_type="application/json",
        )

        self.client.place(
            place_id = self.id,
            fields=["name", "formatted_address", "formatted_phone_number","website"],
            language=self.language,
        )

        # self.assertEqual(1, len(responses.calls))
        # self.assertURLEqual(
        #     "%s?placeid=ChIJR1FOdUXc3IARKmVfLmfjg48&language=en"
        #     "&key=%s&fields=name,formatted_address,formatted_phone_number,type,website"
        #     % (url, self.key),
        #     responses.calls[0].request.url,
        # )
        
        #print(responses.calls[0].request.url)
        with urllib.request.urlopen(responses.calls[0].request.url) as url:
            config.detailsJson = json.loads(url.read().decode())
            #print(config.detailsJson)
            #print(type(config.detailsJson))
            #print(config.detailsJson['result']['website'])
            
        
# detailTest = PlacesDetailTest()
# detailTest.setUp()
# detailTest.test_get_info()
