from django.shortcuts import render
import json
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import loaCrawling


class loaCrawlingView(APIView):

    def post(self, request):
        # HTTP GET Request
        req = requests.get('https://lostark.game.onstove.com/Shop/Mari')

        # GET HTTP Source
        html = req.text

        # Html Parsing
        soup = BeautifulSoup(html, 'html.parser')

        # Copy Selector
        # listItems > li:nth-child(1) > div > div.item-desc > span.item-name
        # listItems > li:nth-child(1) > div > div.area-amount > span
        mari1_item = soup.select('listItems > li:nth-child(1) > div > div.item-desc > span.item-name')
        mari1_cristal = soup.select('listItems > li:nth-child(1) > div > div.area-amount > span')
        mari2_item = soup.select('listItems > li:nth-child(2) > div > div.item-desc > span.item-name')
        mari2_cristal = soup.select('listItems > li:nth-child(2) > div > div.area-amount > span')

        mari3_item = soup.select('listItems > li:nth-child(3) > div > div.item-desc > span.item-name')
        mari3_cristal = soup.select('listItems > li:nth-child(3) > div > div.area-amount > span')

        mari4_item = soup.select('listItems > li:nth-child(4) > div > div.item-desc > span.item-name')
        mari4_cristal = soup.select('listItems > li:nth-child(4) > div > div.area-amount > span')

        mari5_item = soup.select('listItems > li:nth-child(5) > div > div.item-desc > span.item-name')
        mari5_cristal = soup.select('listItems > li:nth-child(5) > div > div.area-amount > span')

        mari6_item = soup.select('listItems > li:nth-child(6) > div > div.item-desc > span.item-name')
        mari6_cristal = soup.select('listItems > li:nth-child(6) > div > div.area-amount > span')

        mariList = ((mari1_item, mari1_cristal), (mari2_item, mari2_cristal), (mari3_item, mari3_cristal),
                    (mari4_item, mari4_cristal), (mari5_item, mari5_cristal), (mari6_item, mari6_cristal))

        print(mariList)

        # for item in mariList:
        #     loaCrawling(item[0].text, item[1].integer).save()

        return Response(data=mariList, status=status.HTTP_201_CREATED)
