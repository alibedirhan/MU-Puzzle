import Instructions
import help
import sys


class MU:

    def __init__(self, my_str="MI", rule="", newStr=""):
        print("Creating Mu class...")
        self.my_str = my_str
        self.rule = rule
        self.newStr = newStr

    @staticmethod
    def instruction():
        print(Instructions)

    @staticmethod
    def help():
        print(help)

    def rule_one(self):
        self.rule = input("Enter a rule 1-4 or q to quit: ")
        if self.rule == "1" and self.my_str.endswith("I"):
            self.newStr = "".join((self.my_str, "U"))
            print(self.newStr)

    def rule_two(self):
        if self.rule == "2" and self.my_str.startswith("M") and not self.my_str.endswith("I"):
            self.newStr = "".join((self.my_str, self.my_str[1:]))
            print(self.my_str)

    def rule_three(self):
        if self.rule == "3" and "III" in self.my_str:
            self.newStr = self.newStr.replace('III', 'U')

    def rule_four(self):
        if self.rule == "4" and "UU" in self.my_str:
            self.newStr = self.newStr.replace('UU', '')

    def error(self):
        pass


call = MU
