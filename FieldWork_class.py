import numpy as np

class FieldWork:

    def __init__(self, data):
        self.data = data

    def calculate_dip_strike(self):
        dip_mean = np.mean(self.data["dip"])
        strike_mean = np.mean(self.data["strike"])

        print(f"The average strike is {strike_mean} degrees")
        print(f"The average dip is {dip_mean} degrees")
        
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
    
    def calculate_top_xy_coordinate(self, grid,x_bottom, y_bottom, angle_degrees):
        
        self.grid_size = (grid.shape[1], grid.shape[0])  # (x_max, y_max)
        angle_radians = np.radians(angle_degrees)
        x_max, y_max = self.grid_size

        L_top = y_max / np.sin(angle_radians)
        L_right = (x_max - x_bottom) / np.cos(angle_radians)

        L = min(L_top, L_right)

        delta_x = L * np.cos(angle_radians)
        delta_y = L * np.sin(angle_radians)

        x_top = x_bottom + delta_x
        y_top = y_bottom + delta_y

        x_top = min(x_top, x_max)
        y_top = min(y_top, y_max)

        return (x_top, y_top)





