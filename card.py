#!/usr/local/bin/python3

class Card(object):
	def __init__(self,suit, number):
		self.suit=suit
		self.number=number

	def __str__(self):
		return f"{self.suit} of {self.number}"


if __name__ == "__main__":
	a = Card(3,5)
	print(a)