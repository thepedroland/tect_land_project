import numpy as np


class FieldWork:

    def __init__(self, data):
        self.data = data

    def calculate_dip_strike(self):
        dip_mean = np.mean(self.data["dip"])
        strike_mean = np.mean(self.data["strike"])

        print(f"The average strike is {strike_mean}")
        print(f"The average dip is {dip_mean}")
        
        return dip_mean

    def calculate_grid_size(self, x_size, y_size, dx, dy):
        self.x_size = x_size
        self.y_size = y_size
        self.dx = dx
        self.dy = dy

        self.rows = self.y_size / self.dy
        self.col = self.x_size / self.dx

        print(f"Your area has {self.x_size} km x {self.y_size} km, the grid has {self.rows} rows and {self.col} columns")
        
        return self.rows, self.col





