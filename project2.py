import numpy as np
import code.voxel_generator as DISPLAY_HANDLER
import code.compute as COMPUTE

def make_state():
    cell_states = ["Uninfected Cells", "Infected Cells", "Dead Cells", "Burst Cell"]

    burst_time = 1 hr
    burst_size = 511

    tumors = (
        GR : (0.03230),     # Growth rate
        Td : (0.0071),      # Death rate
        LAG : (78.9)        # Lag time
    )

    viruses = (
        Virus: ("NDV", "RV", "PV"),
        Name: ("Newcastle Disease Virus", "Reovirus", "Parvo Virus"),
        Infection : (0.981e-8, 0.879e-8, 0.346e-8),                     # Virions per hour
        Release : (511, 626, 98),                                       # Virions per infected cell per hour
        CL : (.00216, 0.00482, 0.106)                                   # 1/h
    )



def update_func():
    pass



def main():
    state = make_system(tumor = "triple-negative-breast-cancer",
                       virus = "NDV",
                       kernel = "kernels/voxel-virus.cl"
                       tumor_factors = {},
                       virus_factors = {},
                   )

    system = make_state(size = (500, 500, 10),
                        virus_placement = ["injection", "culstered", "diffuse"][0],
                        cell_state_array = None,
                        )

    simulation = COMPUTE.NEW_SIMULATION(state = state,
                                        system = system)

    results = simulation.SIMULATE(t0 = 0,
                                  t_final = 70 * (24 * 60 * 60),  #seconds
                                  )

    DISPLAY_HANDLER.DISPLAY_RESULTS(results,
                                    display_items = ["Tumor Cells", "Virus Titer"],
                                    time = [0, -1],
                                    total_points = 10000
                                    )


if __name__ == 'main':
    main()
