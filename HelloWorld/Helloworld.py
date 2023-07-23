def hello_world(name):
    """Function Purpose ::: Add Hello as prefix in front of name """

    print(f"HELLO {name} GOOD MORNING !!!!!!!!!!")


if __name__ == '__main__':
    print("-----Program starts from this line -----")

    name = str(input("Please Enter your name here::::::"))

    # Function call
    hello_world(name)
