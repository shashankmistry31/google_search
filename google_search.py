#! python3

import webbrowser ,sys ,pyperclip

if len(sys.argv) >1 :
    search_term = ''.join(sys.argv[1:])
else:
    search_term = pyperclip.paste()

webbrowser.open("https://www.google.com.tr/search?q={}".format(search_term))
