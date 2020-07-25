from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.espn.com/espnradio/feeds/rss/podcast.xml?id=14554755"
url2 = "https://www.espn.com/espnradio/feeds/rss/podcast.xml?id=26150534"
url3 = "https://www.espn.com/espnradio/feeds/rss/podcast.xml?id=29093703"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.megaphone.fm/96ITpFeyoyyiQy2NJ9w-q-ufr8KwygAAlcfQAEwjqzg/plain/s3://megaphone-prod/podcasts/eff766c2-63ae-11ea-9caa-8b87e9a0e007/image/i.png"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://images.megaphone.fm/8dpYB004gObd1D-vTb4AlUu89AHwvnbIRNI2id8YgBc/plain/s3://megaphone-prod/podcasts/fa218736-63ae-11ea-ac9a-d3f5c62c7dfb/image/1x1.png"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://images.megaphone.fm/KYSKCfEhI98NpDQRkP-Ilp02VLeNXdECkbVDahTbI50/plain/s3://megaphone-prod/podcasts/33397b00-8a47-11ea-ac66-03158d9d3be0/image/1x1.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
