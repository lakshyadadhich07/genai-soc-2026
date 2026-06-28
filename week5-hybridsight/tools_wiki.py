from wikipedia import summary
from langchain_core.tools import tool


@tool
def wiki_search(
    query: str
) -> str:
    """
    Search Wikipedia.

    Use for:
    - historical facts
    - general knowledge
    - concepts
    """

    try:

        result = summary(

            query,

            sentences=4

        )

        return result

    except Exception as e:

        return str(e)