# '''
# in this script we will create a simple program to generate silly stories
# To begin with, we will generate simple sentence as follows:
# "Today, a ninja flew to Mars with a rubber chicken to dance."
# "Today, [character] flew/went [place] with [object] to [action]."
# '''
# from random import choice
# #choice() works in such a way that you pass a list and it gives you random element from it

# character = ["a ninja", "a ballerine", "a student", "a dragon", "a boy", "a girl"]
# place = ["on the moon", "to Mars", "to Atlantis", "to Krypton", "to Hogwarts" "in  a haunted house"]
# object = [" a rubber chicken", "a duck", "a wand", "a banana", "a liquid pizza"]
# action = ["started dancing", "fell asleep", "won the lottery", "started coding", "started drinking"]


# #start = f"Today, {choice(character)} went {choice(place)} with {choice(object)} to {choice(action)}
# '''
# Task 1: Ask user how many sentences do we want to generate and
# then generate those many sentences.
# Task 2:We want to have variation in the sentence that we generate.
# I provide you some sample. You must also randomize those genertion.
# 1.Today a monkey went to jupiter
# '''

# character = ["a ninja", "a ballerine", "a student", "a dragon", "a boy", "a girl"]
# place = ["on the moon", "to Mars", "to Atlantis", "to Krypton", "to Hogwarts", "in  a haunted house"]
# object = [" a rubber chicken", "a duck", "a wand", "a banana", "a liquid pizza"]
# action = ["start dancing", "fell asleep", "won the lottery", "start coding", "start drinking"]

# def generate ():
#     template = [
#         f" Today, {choice(character)} went {choice(place)} and {choice(action)}",
#         f" Once upon a time, {choice(character)} went {choice(place)} with {choice(object)} and {choice(action)}",
#         f" Every monday, {choice(character)} goes {choice(place)} to {choice(action)} with {choice(character)}",
#     ]
#     return template

# sen = (int(input("how many sentences do yo want to print out?: ")))
# while sen > 0:
#     # template = [
#     #     f" Today, {choice(character)} went {choice(place)} and {choice(action)}",
#     #     f" Once upon a time, {choice(character)} {choice(action)} a {choice(object)} and {choice(action)}",
#     #     f" Every monday, {choice(character)} goes {choice(place)} to {choice(action)} with {choice(character)}",]
#     print(choice(generate()))
#     sen -= 1

# sen = int(input("enter a number of sentences: "))
# add = input("input", b)
# b = ("beggining of the sentence", "charater", "place")
 