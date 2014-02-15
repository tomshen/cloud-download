cloud-download
==============

Get direct download links from shared cloud service links.

## Supports
* Dropbox
* Google Drive (only if permissions set to "Anyone who has the link can view")

## CLI
Run
```sh
$ ./download.py dropbox https://www.dropbox.com/s/<...>
```
or
```sh
$ ./download.py drive https://docs.google.com/document/d/<...>
```
to download the file at that shared URL as a PDF to the current directory.

## Python
```python
>>> from download import *
>>> get_dropbox_download_info('https://www.dropbox.com/s/<...>')
('https://dl.dropboxusercontent.com/s/<...>?dl=1&token_hash=<...>', '<...>.pdf')
>>> get_google_drive_download_info('https://docs.google.com/document/d/<...>')
(u'https://docs.google.com/feeds/download/documents/export/Export?id=<...>&exportFormat=pdf', u'<...>.pdf')
```
