import wikipedia
if "wikipedia" in query:
    query = query.replace("on wikipedia","")
    query = query.replace("wikipedia","")
    query = query.replace("search","")
    say(f"searching {query} on wikipedia")
    results = wikipedia.summary(query,sentences = 2)
    say("here are the results")
    print(results)
    say(results)
    
    
