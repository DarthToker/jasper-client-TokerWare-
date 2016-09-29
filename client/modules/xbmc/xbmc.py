# -*- coding: utf-8 -*-

from xbmcjson import XBMC, PLAYER_VIDEO
#Login with default xbmc/xbmc credentials
#xbmc = XBMC("http://YOURHOST/jsonrpc")

#Login with custom credentials
xbmc = XBMC("http://192.168.42.142/jsonrpc", "darthtoker", "Garfield76")

#print xbmc.JSONRPC.Ping()

#xbmc.Input.Info()
#xbmc.GUI.ActivateWindow(window="home")
#xbmc.GUI.ShowNotification({"title":"love you", "message":"I love candy"})
xbmc.Application.SetMute(mute = False)
#xbmc.Application.SetMute(mute = True)
#xbmc.Player.PlayPause({"playerid":1, "play":False})
#xbmc.Player.PlayPause({"playerid":1, "play":True})
#xbmc.Player.PlayPause({"playerid":1})
#xbmc.Player.Stop({"playerid":1})
#xbmc.Player.GoTo({"playerid":1, "to":"next"})
#xbmc.Player.GoTo({"playerid":1, "to":"previous"})
#xbmc.Input.ShowOSD()
#xbmc.Player.SetShuffle({"playerid":1, "shuffle":False})
#xbmc.Player.SetShuffle({"playerid":1, "shuffle":True})
#xbmc.GUI.ActivateWindow({"window":"video"})
#xbmc.Input.ShowCodec()
#xbmc.Player.SetSubtitle({"playerid":1, "subtitle":"on"})
#xbmc.VideoLibrary.GetTVShows() 
