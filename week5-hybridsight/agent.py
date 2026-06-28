from tools_rag import search_documents
from tools_web import web_search
from tools_wiki import wiki_search


def ask_agent(query):

    q = query.lower()

    try:

        if (

            "latest" in q
            or
            "today" in q
            or
            "news" in q

        ):

            result = web_search.invoke(
                query
            )

            return (

                f"""
Tool Used:
Web Search


Answer:

{result}
"""
            )


        if (

            "what is" in q
            or
            "who is" in q
            or
            "history" in q

        ):

            result = wiki_search.invoke(
                query
            )

            return (

                f"""
Tool Used:
Wikipedia


Answer:

{result}
"""
            )


        result = search_documents.invoke(
            query
        )

        return (

            f"""
Tool Used:
RAG


Answer:

{result}
"""
        )

    except Exception as e:

        return str(e)