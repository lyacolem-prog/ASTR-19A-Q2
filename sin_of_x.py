from tabulate import tabulate
import numpy as np


x = np.linspace(0, np.pi*2, 1000) 
sin_x = np.sin(x) 

table_data = [(a, b) for a, b in zip(x, sin_x)]

table_headers = ["x", "sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers, floatfmt=".3f")

def main():
    print(python_table)

if __name__=='__main__':
    main()


