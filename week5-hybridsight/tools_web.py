from ddgs import DDGS
from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """
    Search live web.

    Use for:
    - current events
    - latest information
    - internet lookup
    """

    try:

        results = []

        with DDGS() as ddgs:

            data = list(

                ddgs.text(

                    query,

                    max_results=5

                )

            )

        if len(data) == 0:

            return (
                "No web results found."
            )

        for i, r in enumerate(
            data,
            start=1
        ):

            title = r.get(
                "title",
                ""
            )

            body = r.get(
                "body",
                ""
            )

            results.append(

                f"""

Result {i}

Title:
{title}

Body:
{body}

"""

            )

        return "\n".join(
            results
        )

    except Exception as e:

        return str(e)