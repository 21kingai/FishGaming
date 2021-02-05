import wx
import menu
import os

SCREENWIDTH = 240
SCREENHEIGHT = 180

app = wx.App()

frame = wx.Frame(None, title='Test')
frame.SetSize(0, 0, SCREENWIDTH, SCREENHEIGHT)
pnl = wx.Panel(frame)


def buttonpress(event):
    menu.runfishgaming()

forButton = wx.Button(pnl, label='Run', pos=(185, 110))
forButton.SetSize(25, 25)
forButton.Bind(wx.EVT_BUTTON, buttonpress)


frame.Show()

app.MainLoop()
