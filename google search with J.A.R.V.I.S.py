import webbrowser
elif "search" in query and "google" in query:
        query = query.replace("search","")
        query = query.replace("on google","")
        query = query.replace("google","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"

        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")