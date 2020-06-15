import unittest
import JsonParsing
import json


class Tests(unittest.TestCase):
    def testChangingColor(self):
        JsonParsing.main("test.json", "changesColor")
        with open("newJson.json") as f:
            r = json.load(f)
            self.assertEqual(r["page1"]["initialSettings"]["color"], "green")

    def testChangingsort(self):
        JsonParsing.main("test.json", "changesSort")
        with open("newJson.json") as f:
            r = json.load(f)
            self.assertEqual(r["page1"]["available-filters"]["name-filter"]["sort"], "asc")

    def testChangingCoordinates(self):
        JsonParsing.main("test.json", "changeCoordinates")
        with open("newJson.json") as f:
            r = json.load(f)
            self.assertEqual(r["page1"]["initialSettings"]["coordinates"], [24, 30])

    def testChangingNameFilter(self):
        JsonParsing.main("test.json", "changeNameFilter")
        with open("newJson.json") as f:
            r = json.load(f)
            self.assertEqual(r["page1"]["available-filters"]["name-filter"]["column"], "lastName")

    def testChangingPreciseCoor(self):
        JsonParsing.main("test.json", "changePreciseCoor")
        with open("newJson.json") as f:
            r = json.load(f)
            self.assertEqual(r["page1"]["initialSettings"]["coordinates"][0]["value"], "Wow JSON injected!!")