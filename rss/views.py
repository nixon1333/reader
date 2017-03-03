from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
import feedparser
from .helper import RssHelper

# Create your views here.

class RssManager(APIView):

    def post(self, request, format=None):
        # request.user
        if request.user.is_authenticated():
        # Do something for authenticated users.
            requested_feed_url = request.POST.get('url', False)

            # first validate
            if RssHelper.check_requested_data_for_rss_save(requested_feed_url):

                check_url_get_title = RssHelper.url_validate(self, requested_feed_url)
                if check_url_get_title:
                    #now save the data
                    feed_data = {}
                    feed_data['url'] = requested_feed_url
                    feed_data['user'] = request.user
                    feed_data['title'] = check_url_get_title

                    confirm_res = RssHelper.save_rss_feed(self, feed_data)
                    if confirm_res['success']:
                        return JsonResponse({
                            'success': True,
                            'message': 'Feed Created'
                        })

                    return JsonResponse({
                        'success': False,
                        'message': confirm_res['reason']
                    })
                return JsonResponse({
                    'success': False,
                    'message': 'Url is not a valid url'
                })

            return JsonResponse({
                'success': False,
                'message': 'url parameter missing'
            }, safe=False)
        else:
        # Do something for anonymous users.
            return JsonResponse({
                'success':False,
                'message' : 'You are not permitted'
            }, safe=False)

    def get(self, request, format=None):

        if request.user.is_authenticated():

            requested_url_id = request.GET.get('url_id', False)

            rss_data = RssHelper.get_rss_feed_or_list(requested_url_id, request.user)



            return JsonResponse({
                'success': True,
                'url_id': requested_url_id,
                'data':rss_data
            }, safe=False)

        return JsonResponse({
                'success': False,
                'message': 'You are not permitted'
            }, safe=False)


