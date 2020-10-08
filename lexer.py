
import re

from token import Token
import token_types



class Lexer:

    def __init__(self, text):
        self.text = text
        self.current_character = None
        self.digits = "01234567890"
        self.current_position = -1
        self.next_char()

    def next_char(self):
        self.current_position += 1 
        self.current_character = self.text[self.current_position
            ] if self.current_position < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_character is not None:
            if self.current_character in [' \t', ' ']:
                self.next_char()
                continue
            elif self.current_character in ["'", '"']:
                tokens.append(self.make_string())
            elif re.match("[_a-zA-Z]", self.current_character):
                tokens.append(self.make_variable())
                continue
            elif self.current_character in self.digits:
                tokens.append(self.make_number())
                continue
            elif self.current_character == "=":
                tokens.append(Token(token_types.ASSIGNMENT))
            elif self.current_character == "+":
                tokens.append(Token(token_types.PLUS))
            elif self.current_character == "-":
                tokens.append(Token(token_types.MINUS))
            elif self.current_character == "*":
                tokens.append(Token(token_types.MUL))
            elif self.current_character == "/":
                tokens.append(Token(token_types.DIV))
            elif self.current_character == '(':
                tokens.append(Token(token_types.R_PARANTESES))
            elif self.current_character == ")":
                tokens.append(Token(token_types.L_PARANTESES))
            else:
                error_details = "'" + self.current_character + "'"
                return [], None
            self.next_char()
        return tokens, None

    def make_number(self):
        number_string = ""
        number_of_dot = 0

        while (self.current_character is not None and 
            self.current_character in self.digits + "."):
            if self.current_character == ".":
                if number_of_dot == 1:
                    break
                number_string += self.current_character
                number_of_dot += 1
            else:
                number_string += self.current_character
            self.next_char()

        if number_of_dot == 0:
            return Token(token_types.INT, int(number_string))
        return Token(token_types.FLOAT, float(number_string))

    def make_variable(self):
        variable_name = self.current_character
        self.next_char()
        while(self.current_character is not None and
            re.match('[_a-zA-Z0-9]', self.current_character)):
            variable_name += self.current_character
            self.next_char()
        return Token(token_types.VAR_NAME, variable_name)

    def make_string(self):
        delimeter = self.current_character
        string = ""
        self.next_char()
        while(self.current_character != delimeter):
            string += self.current_character

            self.next_char()
            if self.current_character is None:
                raise Exception("Invalid syntax")
        return Token(token_types.STRING)
