#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
import os

def generate_graph(file_path):
	with open(file_path, 'r') as dat_file:
		reader = csv.reader(dat_file, delimiter=' ')
		x = []
		y = []
		row_num = 1
		for row in reader:
			if row_num >=15:
				x.append(int(row[0]))
				y.append(int(row[1]))
			row_num += 1
	ax = plt.gca()
	ax.set_aspect(aspect=60)
	plt.xlabel('CCD Pixel Number')
	plt.ylabel('Intensity (r.u.)')
	plt.plot(x, y, color="blue", linewidth=0.5)
	plt.savefig(file_path[:-4] + ".png")

if __name__ == "__main__":
	dir_path = os.path.dirname(os.path.realpath(__file__))
	for filename in os.listdir(dir_path):
		if filename.endswith(".dat"):
			print(filename)
			generate_graph(filename)
