import webbrowser

def open_url (url):
    if url:
        webbrowser.open(f'{url}')
        return 'successfully opened Website'
    else:
        return 'Cannot open this url'
