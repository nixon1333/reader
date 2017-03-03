import urllib.request as req
from .models import *
import feedparser

class RssHelper:


    def check_requested_data_for_rss_save(requested_data):
        if requested_data:
            return True
        return False

    def url_validate(self,url_to_check):
        try:
            request = req.Request(url_to_check)
            req.urlopen(request)
            feed_data = feedparser.parse(url_to_check)
            if len(feed_data['entries']) > 0 :
                return feed_data['feed']['title']
            return False
        except:
            return False

    def save_rss_feed(self, feed_info):
        try:
            if RssHelper.check_if_exits(feed_info['url'], feed_info['user']):
                return {
                    'success': False,
                    'reason': 'Already Saved'
                }

            # first check if previously added save data
            feed_list = FeedsList()
            feed_list.user = feed_info['user']
            feed_list.url = feed_info['url']
            feed_list.name = feed_info['title']
            feed_list.save()
            return {
                'success': True,
            }
        except:
            return {
                'success': False,
                'reason': 'Something went wrong'
            }

    def check_if_exits(url_add, user):

        if len(FeedsList.objects.filter(url=url_add,user=user).values()) > 0:
            return True
        return False
