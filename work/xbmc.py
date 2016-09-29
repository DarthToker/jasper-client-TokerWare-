
from xbmcjson import XBMC, PLAYER_VIDEO
#Login with default xbmc/xbmc credentials
xbmc = XBMC("http://YOURHOST/jsonrpc")

#Login with custom credentials
xbmc = XBMC("http://192.168.42.142/jsonrpc", "darthtoker", "Garfield76")

#print xbmc.JSONRPC.Ping()

#xbmc.Input.Info()
#xbmc.GUI.ActivateWindow(window="home")
xbmc.GUI.ShowNotification({"title":"love you", "message":"I love candy"})
