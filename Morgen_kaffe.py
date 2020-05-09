import webbrowser
import os

webbrowser.open(url = "https://www.vg.no/", new=1, autoraise=True)


x = webbrowser.register(
    "chrome2", None, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    )
controller = webbrowser.get(x)

#os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

def papers():
    
    controller.open_new("https://www.vg.no/")
    #webbrowser.open("https://www.dagbladet.no/", new=0, autoraise=True)
    #webbrowser.open("https://www.nrk.no/", new=2, autoraise=True)
    #webbrowser.open("https://www.aftenposten.no/", new=2, autoraise=True)
    #webbrowser.open("https://e24.no/", new=2, autoraise=True)
    
papers()