import eel
import sys

if sys.argv[1] == 'pc':
    eel.init("web")
    eel.start("index1.html")
elif sys.argv[1] == 'mobile':
    eel.init("web")
    eel.start("index.html", size=(1280, 720))
