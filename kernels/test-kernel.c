#include <stdio.h>

struct Cell {
  int state_id;
};


void compute_interaction( int thread,
                          float4 sim_size,
                          int states[],
                          float state_transitions[]
                          ){


  //["Uninfected Cells", "Infected Cells", "Dead Cells", "Burst Cell"]

  int neighbor_states = [num_states];

  int current_x = thread % sim_size.x;
  int current_y = current_cell.y;
  int current_z = current_cell.z;



  for(int z = (-1 * sim_size.z); z <= sim_size.z, z += sim_size.z){
    

  }




  for(int offset = (-13+current_cell); offset < (14+current_cell); offset++){

    if( !(offset > -1) ){

      neighbor_cell_state = cells[offset];
      neighbor_states[neighbor_cell_state]+= 1;

    }else{
      // Set boundary conditions

    }

  };
}


int main(){

  compute_interaction();
}
