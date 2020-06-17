from django.test import TestCase, Client
from django.conf import settings

# Create your tests here.
from feed_reader.models import Channel, Item
from feed_reader.utils import read_feed

from django.utils import timezone
from django.urls import reverse

from datetime import timedelta

import mock

import os

import requests_mock

TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)),"datatest")
BASE_URL = 'https://feedforall.com/'

class BaseTest(TestCase):
    def _populate_mock(self, mock, test_file, status, content_type, etag=None, headers=None, url=BASE_URL, is_cloudflare=False):
    
        content = open(os.path.join(TEST_DATA, test_file), "rb").read()
        
        
        ret_headers =  {"Content-Type": content_type, "etag":"an-etag"}
        if headers is not None:
            ret_headers = {**ret_headers, **headers}
        
        {"Content-Type": content_type, "etag":"an-etag"}
        
        if is_cloudflare:
            agent = "{user_agent} (+{server}; Updater; {subs} subscribers)".format(user_agent=settings.FEEDS_USER_AGENT, server=settings.FEEDS_SERVER, subs=1)

            mock.register_uri('GET', url, request_headers={"User-Agent": agent}, status_code=status, content=content, headers=ret_headers)
        else:
            if etag is None:
                mock.register_uri('GET', url, status_code=status, content=content, headers=ret_headers)
            else:
                mock.register_uri('GET', url, request_headers={'If-None-Match': etag}, status_code=status, content=content, headers=ret_headers)
                    

@requests_mock.Mocker()
class XMLFeedsTest(BaseTest):
    def test_simple_xml(self, mock):
        settings.configure
        self._populate_mock(mock, status=200, test_file="sample-feed.xml",
                 content_type="application/rss+xml")
        
        # Read the feed once to get the 1 post  and the etag
        feed_result = read_feed(BASE_URL)  
        channel = feed_result.channel   
        self.assertEqual(channel.title, "Sample Feed - Favorite RSS Related Software")
        self.assertEqual(channel.description, "Take a look at some of FeedForAll&apos;s favorite software and resources for learning more about RSS.")
        self.assertEqual(channel.language, "en-us")

        items = feed_result.items
        self.assertEqual(len(items), 9)
        self.assertEqual(items[0].channel.id, channel.id)
        self.assertEqual(items[0].title, "RSS Resources")
