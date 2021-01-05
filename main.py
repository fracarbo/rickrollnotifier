class YtVideo:

    def __init__(self, id):
        self.id = id

    def getViews(self):
        try:
            import requests
            API_KEY = ""
            api_string = "https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=statistics" % (self.id, API_KEY)
            data = requests.get(api_string).json()
            views = data['items'][0]['statistics']['viewCount']
            return views
        except:
            print('Error')

    def someoneWatched(self):
        import time

        views = self.getViews()
        while True:
            time.sleep(10)
            updated_views = self.getViews()
            if updated_views > views:
                return True
            views = updated_views

def notify_me(title = 'Watched', desc = 'Someone watched your video'):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, desc)
    except:
        print(title)
        print(desc)  

if __name__ == "__main__":
    VIDEO_ID = 'dQw4w9WgXcQ'
    video = YtVideo(VIDEO_ID)
    print('Waiting...')
    while True:
        if video.someoneWatched():
            notify_me('Rickrolled', 'Someone has been rickrolled!')