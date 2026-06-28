from agent import ask_agent


while True:

    q = input(
        "\nAsk: "
    )

    if q.lower() == "exit":

        break

    print()

    print(

        ask_agent(
            q
        )

    )