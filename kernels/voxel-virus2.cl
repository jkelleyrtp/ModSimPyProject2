inline int neighbor_state_counts(__global uint* cells, uint4 sim_size, int thread){
  int cell = 0;
  int cell_states[] = {0,0,0,0};
  int cell_state;
  //uint ssx = sim_size.x;
  //uint ssy = sim_size.y;
  //uint ssz = sim_size.z;



  for(int z = -1; z <= 1; z++){
    for(int y = -1; y <= 1; y++){
      for(int x = -1; x <= 1; x++){
        cell = (thread + x + y *sim_size.y + z*(sim_size.y * sim_size.x));
        // Check if in bounds
        if(cell > -1 && cell < sim_size.y * sim_size.x * sim_size.z){
          //cell_states[0] += 1;

          cell_state = cells[cell];
          cell_states[cell_state] += 1;
        }
        //cell += (thread + x + y * ssy + z*(ssy * ssx));
      }
    }
  }
  return cell_states[0];
}



__kernel void compute_interaction(__global uint* cells,
                                  __global int* results,
                                  uint4 sim_size
          ){

  unsigned int thread = get_global_id(0);
  results[thread] = neighbor_state_counts(cells, sim_size, thread);
  //results[thread] = 1;

}
