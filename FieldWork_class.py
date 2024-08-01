import numpy as np

class FieldWork:

    def __init__(self,data):

        self.data = data

        pass
    
    def calculate_dip_strike(self,dip_mean,strike_mean):

        self.data = data

        self.dip_mean = np.mean(data["dip"])
        self.strike_mean = np.mean(data["strike"])

        print(f"The average strike is {strike_mean}")
        print(f"The average dip is {dip_mean}")

        pass

    def calculate_grid_size(self,w,l,dx):
        
        self.w = w
        self.l = l
        self.dx = dx

        rows = l/dx
        col = w/dx

        print(f"Your area have {w}x{l}, the grid has {rows} rows and {col} columns")

        pass



