import webbrowser
'''
GOOGLESEARCHLINK = "https://www.google.com/search?q="

user_term = input("Enter a search term: ")

user_term = user_term.strip()

user_term = user_term.replace(" ", "+")

user_search = GOOGLESEARCHLINK + user_term

webbrowser.open(user_search)
'''

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)