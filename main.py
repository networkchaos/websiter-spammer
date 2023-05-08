def main():
    import webbrowser
    import time
    import random
    websites = random.choice([
        "youtube.com"
        "spotify.com"
        "dropbox.com"
        "uber.com"
        "google.com"
        "xvideos.com"
        "xnxx.com"
        "pornhub.com"
        ])
    formatted = "https://{}".format(websites)
    while 1:
        webbrowser.open(formatted)
        time.sleep(3)

if __name__ == "__main__":
    main()
    
