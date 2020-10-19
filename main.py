import Instructions
import help
import sys


class MU:

    def __init__(self, my_str="MI", rule="", newStr=""):
        print("Creating Mu class...")
        self.my_str = my_str
        self.rule = rule
        self.newStr = newStr

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
        try:
            if self.rule == "":
                print(help)
        except:
            print("Please enter a rule number")


call = MU


def instruction():
    print(Instructions)


instruction()


def print_key_info():
    print(help)


print_key_info()
MU.rule = input("Enter a combination of M, U and I: ")

while True:
    if MU.rule and all(ch in "MIU" for ch in MU.rule):
        print("This is correct")
        break
    else:
        print("This is incorrect")
        break

MU.help = input("Enter a rule 1-4 or q to quit: ")
