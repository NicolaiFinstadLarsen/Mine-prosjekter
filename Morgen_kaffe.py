import webbrowser


print("Good morning :)")


def open_papers():
    
    webbrowser.open_new("https://www.vg.no/")
    webbrowser.open("https://www.dagbladet.no/", new=2, autoraise=True)
    webbrowser.open("https://www.nrk.no/", new=2, autoraise=True)
    webbrowser.open("https://www.aftenposten.no/", new=2, autoraise=True)
    webbrowser.open("https://e24.no/", new=2, autoraise=True)
    
open_papers()