import webbrowser

def papers():
    
    webbrowser.open_new("https://www.aftenposten.no/")
    webbrowser.open("https://www.nrk.no/", new=2, autoraise=True)
    webbrowser.open("https://e24.no/", new=2, autoraise=True)
    webbrowser.open("https://www.dn.no/", new=2, autoraise=True)
    
    webbrowser.open(
        "https://investor.nordea.no/oetoi/noi/bookmark?time=1590180670578&view=OPEN_MARKET_GLOBAL_VIEW&locale=no_NO&GENID=2ba4b997f2b44e8bbdc8d86f4a9a794d", new=2, autoraise=True
        )
    
    webbrowser.open("https://investor.dn.no/#!/Oversikt", new=2, autoraise=True)
    webbrowser.open("https://www.shareville.no/me/portfolios", new=2, autoraise=True)
    webbrowser.open("https://www.vg.no/", new=1, autoraise=True)
    webbrowser.open("https://www.dagbladet.no/", new=0, autoraise=True)
    
    
papers()