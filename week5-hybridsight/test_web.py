from tools_web import web_search


while True:

    q = input(
        "\nAsk: "
    )

    if q.lower() == "exit":

        break

    print()

    answer = web_search.invoke(
        q
    )

    print(
        answer
    )