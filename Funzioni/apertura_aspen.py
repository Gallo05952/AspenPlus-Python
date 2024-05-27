import win32com.client as win32

class AperturaAspen:

    def __init__(self):
        pass

    
    def apertura(self, path, visible=False):
        self.aspen = win32.Dispatch('Apwn.Document')
        self.aspen.InitFromFile(path, "")
        self.aspen.Visible = visible
        return self.aspen

    def close(self,programma):
        programma.Close()
        del programma