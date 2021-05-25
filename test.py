import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    twitch_name = sys.argv[1]
else:
    twitch_name = pyperclip.paste()

webbrowser.open("https://twitch.tv/"+twitch_name)