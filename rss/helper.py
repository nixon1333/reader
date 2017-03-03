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

        if len(FeedsList.objects.filter(url=url_add,user=user,status=1).values()) > 0:
            return True
        return False

    def get_rss_feed_or_list(rss_url_id,user_id):

        if rss_url_id:
            feed_data = RssHelper.get_rss_details(rss_url_id,user_id)
            return {
                'feed' : feed_data
            }
        else:
            rss_data = list(FeedsList.objects.filter(user=user_id, status=1).values('url','name','id'))
            return {
                'list' : rss_data
            }

    def get_rss_details(rss_url_id,user_id):

        feed_url_data = FeedsList.objects.filter(id=rss_url_id,user=user_id,status=1).values()
        if feed_url_data.first():
            feed_url = feed_url_data.first()['url']
            parsed_data = feedparser.parse(feed_url)
            return {
                'feed_name': parsed_data['feed']['title'],
                'feed_details': parsed_data['feed']['subtitle'],
                'feed_link': parsed_data['feed']['link'],
                'feed_updated': parsed_data['feed']['updated'],
                'feed_entries': parsed_data['entries'],
            }
        return {

        }
