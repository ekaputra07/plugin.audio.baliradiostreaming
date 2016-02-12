import sys
import xbmcplugin
import xbmcgui

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')

# Radio directory
stations = (
    ('Gita Bali Internet Radio', 'http://gitabali.listenon.in:8038/listen.pls'),
    ('Menara FM Bali', 'http://server.menara-fm.com:10280/menarafmbali'),
    ('Hard Rock Radio Bali', 'http://indo.mra.rastream.com:80/mra_hardrock-bali?type=.flv'),
    ('CDBS FM', 'http://103.28.148.18:8136/listen.pls'),
    ('Pinguin FM', 'http://radiopinguinfm.com/streaming/listen.pls'),
    ('OZ Radio Bali', 'http://radio.simaya.net.id:1320/listen.pls'),
    ('FBI FM Bali', 'http://server.fbifm.com:9180/fbibaliradio'),
    ('Radio Barong Singaraja', 'http://stream.suararadio.com:8000/singaraja_barong_mono'),
    ('Radio AR Bali', 'http://radioarbali.com/streaming/listen.pls'),
)

# Create the station list
for station in stations:
    li = xbmcgui.ListItem(station[0])
    li.setInfo('music', {'artist': station[0]})
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=station[1], listitem=li)

# End the list
xbmcplugin.endOfDirectory(addon_handle)
