import webbrowser
if "search" in query and "youtube" in query :
        query = query.replace("search","")
        query = query.replace("on youtube","")
        query = query.replace("youtube","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")