import webbrowser, sys

sys.argv

if len(sys.argv) > 1:
    twitch_name = sys.argv[1]

webbrowser.open("https://twitch.tv/"+twitch_name)

