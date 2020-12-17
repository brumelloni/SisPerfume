import wx
from ProjSisPerfumesFramePrincipal import ProjSisPerfumesFramePrincipal
if __name__ == '__main__':
    app=wx.App()
    framePrincipal=ProjSisPerfumesFramePrincipal(None)
    framePrincipal.Show(True)
    app.MainLoop()