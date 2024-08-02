import numpy as np

class FieldWork:

    def __init__(self,data):

        self.data = data

    def calculate_dip_strike(self):

        dip_mean = np.mean(self.data["dip"])
        strike_mean = np.mean(self.data["strike"])

        print(f"The average strike is {strike_mean}")
        print(f"The average dip is {dip_mean}")
        
        return dip_mean

    def calculate_grid_size(self,x_size,y_size,dx,dy):

        self.w = w
        self.l = l
        self.dx = dx

        rows = l/dx
        col = w/dx

        print(f"Your area have {w}x{l}, the grid has {rows} rows and {col} columns")
        
        return rows, col




