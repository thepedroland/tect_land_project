import os
from landlab.components import NormalFault
from landlab import RasterModelGrid, imshow_grid
import matplotlib.pyplot as plt 
import numpy as np 

def running_normal_fault(basin_fault_mg,uplift_rates,dip_angle,bottom_xy_coord,top_xy_coord,n_steps,dt,scenario,fa,ld,sp):
    folder_name = f'model_fault_scenario_{scenario}'
    os.makedirs(folder_name, exist_ok=True)
    
    up = uplift_rates[scenario]
    by = bottom_xy_coord[1]
    bx= bottom_xy_coord[0]
    ty= top_xy_coord[1]
    tx= top_xy_coord[0]
    params_fault = {
                "faulted_surface": "topographic__elevation",
                "fault_dip_angle": dip_angle,
                "fault_throw_rate_through_time": {
                    "time": [100000],
                    "rate": [up],
                },
                "fault_trace": {"y1": bottom_xy_coord[1], "x1": bottom_xy_coord[0], "y2": top_xy_coord[1], "x2": top_xy_coord[0]},
                "include_boundaries": True,
            }

    nf= NormalFault(basin_fault_mg,**params_fault)
    
    for i in range(n_steps):

        fa.run_one_step()
        sp.run_one_step(dt=dt)
        ld.run_one_step(dt)
        nf.run_one_step(dt)

        if i%1000 == 0:
            imshow_grid(basin_fault_mg, 'topographic__elevation')
            plt.show()
            print(i)
            
            filename = os.path.join(folder_name, f"model_teton_fault_in_year_{i*dt}.txt")
            np.savetxt(filename,basin_fault_mg.at_node['topographic__elevation'])            