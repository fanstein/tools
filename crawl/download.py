import requests
import urllib2

# http://httpstat.us


def download(url, num_retries=2):
    print 'downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                return download((url, num_retries - 1))
    return html
