#!/usr/bin/env python
import sys
import urllib2

def get_url(url):
    req = urllib2.Request(url)
    return urllib2.urlopen(req).fp.read()

def download_url(url, file_name):
    with open(file_name, 'w') as f:
        f.write(get_url(url))

DROPBOX_BASE_URL = 'https://dl.dropboxusercontent.com'
def get_dropbox_download_info(url):
    page = get_url(url)
    download_token_index = page.index('token_hash') + 11
    download_token = page[download_token_index:page.index('"',
        download_token_index)]
    download_url = '%s%s?dl=1&token_hash=%s' % (DROPBOX_BASE_URL,
        url.split('dropbox.com')[1], download_token)
    file_name = url.split('/')[-1]
    return download_url, file_name

GOOGLE_DRIVE_BASE_URL = 'https://docs.google.com/feeds/download/documents/export/Export?id='
def get_google_drive_download_info(url):
    file_id = url.split('d/')[1].split('/')[0]
    download_url = GOOGLE_DRIVE_BASE_URL + file_id + '&exportFormat=pdf'
    file_name = file_id + '.pdf'
    return download_url, file_name

if __name__ == '__main__':
    if sys.argv[1] == 'dropbox':
        url = sys.argv[2]
        download_url(*get_dropbox_download_info(url))
    elif sys.argv[1] == 'drive':
        url = sys.argv[2]
        download_url(*get_google_drive_download_info(url))