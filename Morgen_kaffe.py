import webbrowser



for i in range(1,2):
    
    chrome_path1 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --profile-directory="Profile '+str(i)+'" %s'
   
    webbrowser.get(chrome_path1).open("https://www.nrk.no/")
    
    webbrowser.open("https://e24.no/", new=0, autoraise=True)
    webbrowser.open("https://www.dn.no/", new=2, autoraise=True)
    
    webbrowser.open(
        "https://investor.nordea.no/oetoi/noi/bookmark?time=1590180670578&view=OPEN_MARKET_GLOBAL_VIEW&locale=no_NO&GENID=2ba4b997f2b44e8bbdc8d86f4a9a794d", new=2, autoraise=True
        )
    webbrowser.open("https://www.nordnet.no/no", new=2, autoraise=True)
    webbrowser.open("https://investor.dn.no/#!/Oversikt", new=2, autoraise=True)
    webbrowser.open("https://www.shareville.no/me/portfolios", new=2, autoraise=True)
    webbrowser.open("https://www.euronextvps.no/", new=2, autoraise=True)
    webbrowser.open("https://www.vg.no/", new=2, autoraise=True)
    webbrowser.open("https://www.dagbladet.no/", new=2, autoraise=True)
    
    
    