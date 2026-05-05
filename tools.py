from ddgs import DDGS

def web_search(query):
    try:
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for r in search_results:
                title = r.get("title", "")
                body = r.get("body", "")
                href = r.get("href", "")
                results.append(f"Title: {title}\nSummary: {body}\nURL: {href}")

        if not results:
            return "No web search results found."

        return "\n\n".join(results)

    except Exception as e:
        return f"Web search error: {str(e)}"