import wx

class XinFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'jinliang',size=(400,400))
		label = wx.StaticText(self,-1,'Hello wxPython',(100,10))
		label.SetBackgroundColour('black')
		label.SetForegroundColour('white')

		text = wx.StaticText(self,-1,'jinliang',(100,50),(160,-1),wx.ALIGN_CENTER)
		text.SetForegroundColour('green')
		text.SetBackgroundColour('yellow')


app = wx.App()
xframe = XinFrame()
xframe.Show()
app.MainLoop()

