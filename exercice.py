#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
# Question 1
def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAXES = 0.15

# Calculer le sous-total
	sous_total = 0
	for item in data:
		sous_total = sous_total + item[INDEX_QUANTITY] * item[INDEX_PRICE]

# Calculer taxes
	taxe = sous_total * TAXES

# Calculer le total
	total = sous_total + taxe

# La facture
	facture = [
		("SOUS-TOTAL", sous_total),
		("TAXES", taxe),
		("TOTAL", total)
	]
	result = name
	for bd in facture:
		result += "\n" + f"{bd[0]} {bd[1] : >10.2f} $"

	return result

# Question 2
def format_number(number, num_decimal_digits):

# 1. Séparer partie entière et décimale
	decimal_part = abs(number) % 1			# quand on écrit x % 1, on obtient la partie décimale du nombre x
	whole_part = int(abs(number))           # on peut aussi écrire [abs(number) // 1] pour avoir la partie entière d'un nombre

#1.1 Partie décimale
	decimal_str = str(int(round(decimal_part * 10**num_decimal_digits)))
	decimal_str = "." + decimal_str + "0" * (num_decimal_digits - len(decimal_str))

#1.2 Partie entière

	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part = whole_part // 1000
		whole_part_str = str(whole_part) + whole_part_str

# 2. Coller les deux parties ensembles
	if number < 0:
		x = "-" + whole_part_str + decimal_str
	else:
		"il n'y a rien"
	return x

# Question 3
def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	# Calculer la largeur
	triangle_width = 1 + 2 * (num_rows - 1) # on fait [2*(num_rows - 1)], car on veut qu'il ait des plafonds en haut et en bas du tableau

	# Construire première et dernière ligne (bordures pleines)
	border_row = BORDER_CHAR * (triangle_width + 2)

	# Afficher le triangle
	result = border_row
	# Pour chaque ligne du triangle
	for i in range(num_rows):
		triangle_chars = TRIANGLE_CHAR * (i * 2 + 1)
		result += "\n" + f"{BORDER_CHAR}{triangle_chars : ^{triangle_width}}{BORDER_CHAR}"
	result += "\n" + border_row

	return result




if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
