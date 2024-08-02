def running_normal_fault(basin,uplift_rate,dip_angle,bottom_xy_coord,top_xy_coord,n_steps,dt)

by = bottom_xy_coord[1]
bx= bottom_xy_coord[0]
ty= top_xy_coord[1]
tx= top_xy_coord[0]
    params_fault = {
             "faulted_surface": "topographic__elevation",
             "fault_dip_angle": dip_angle,
             "fault_throw_rate_through_time": {
                 "time": [100000],
                 "rate": [uplift],
             },
             "fault_trace": {"y1": bottom_xy_coord[1], "x1": bottom_xy_coord[0], "y2": top_xy_coord[1], "x2": top_xy_coord[0]},
             "include_boundaries": True,
         }


for i in range(n_steps):
    
    fa.run_one_step()
    sp.run_one_step(dt=dt)
    ld.run_one_step(dt)
    nf.run_one_step(dt)

    if i%1000 == 0:
        imshow_grid(basin_fault_mg, 'topographic__elevation')
        plt.show()
        print(i)
        np.savetxt((f"model_teton_fault in year {i*dt}"),basin_fault_mg.at_node['topographic__elevation'])

        