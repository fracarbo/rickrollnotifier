def getViews(id):
    import requests

    api_key = "AIzaSyB77QZ1ZlIkie1IR7C0LICQyfrE5HmSlcc"
    api_string = "https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=statistics" % (id, api_key)
    data = requests.get(api_string).json()
    views = data['items'][0]['statistics']['viewCount']
    return views

def notify_me(msg = 'Watched'):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast(msg, 'Someone watched your video!')

def someoneWatched(id):
    import time

    views = getViews(id)
    while True:
        time.sleep(10)
        updated_views = getViews(id)
        if updated_views > views:
            return True
        views = updated_views

video_id = 'dQw4w9WgXcQ'
print('Waiting...')
while True:
    if someoneWatched(video_id):
        notify_me("Rickrolled")