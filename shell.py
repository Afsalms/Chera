from lexer import Lexer

print("Chera ")

while True:
    text = input('>>>')
    print(text)
    print(">>>>>>>>>>>>>>.")
    while not text:
        text = input(">>>")
    lexer = Lexer(text)

    try:
        tokens = lexer.make_tokens()
        print(tokens)
    except Exception as e:
        print(e)

    