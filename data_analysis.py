"""
data_analysis.py

- Performs data analysis on data collected in data.txt file.
- Continued in `data_analysis_notebook.py`
"""

import json
import numpy as np

def read_data(f_path):
	"""
	Reads data in from file `f_path`. 
	Expects each line to be string convertible to json.
	"""
	ret_list = []
	# open file and read data in to the array
	with open(f_path) as f:
		for line in f:
			# print(line) # we inserted newline separator after each message received in the server
			try:
				x = json.loads(line)
			except ValueError:
				print("{0} was not proper json".format(line))
			except:
				print("Unexpected Error")
			else:
				# https://www.tutorialspoint.com/python/python_exceptions.htm
				print(x)
				ret_list.append(x)
	return ret_list



if __name__ == "__main__":
	data_list = read_data("./data.txt")

	# now you can do stuff with the data:
	# print("\n\nHERE IS YOUR DATA:\n\n")
	# print(len(data_list))
	# print(data_list[1])

	data = np.array(data_list)
	print(data)