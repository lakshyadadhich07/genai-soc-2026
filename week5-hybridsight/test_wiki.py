from tools_wiki import wiki_search


while True:

    q = input(
        "\nAsk: "
    )

    if q == "exit":

        break

    print()

    print(

        wiki_search.invoke(
            q
        )

    )