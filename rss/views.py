from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
import feedparser

# Create your views here.

class getRssDetails(APIView):
    def get(self, request, format=None):

        parsed_data = feedparser.parse('http://feeds.feedburner.com/300mbfilms1')
        # parsed_data = feedparser.parse('http://www.feedforall.com/blog-feed.xml')

        # print(parsed_data)

        return JsonResponse({
            'success': True,
            'name':parsed_data['feed']['title'],
            'subtitle':parsed_data['feed']['subtitle'],
            'link':parsed_data['feed']['link'],
            'updated':parsed_data['feed']['updated'],
            'entries':parsed_data['entries'],
        }, safe=False)

