#!/usr/bin/python3
# Quickly opens blitz.gg build for a champion
import sys
import webbrowser

base_url = "https://blitz.gg/lol/champions/"
browser_path = "/mnt/c/Program Files/Mozilla Firefox/firefox.exe"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error -- provide name of champion")
        exit(1)

    webbrowser.register('wsl', None,
                        webbrowser.GenericBrowser(browser_path))

    url = base_url + sys.argv[1]
    webbrowser.get('wsl').open(url)
