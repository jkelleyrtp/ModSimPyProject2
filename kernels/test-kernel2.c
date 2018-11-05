#include <stdio.h>

struct vector3 {
  int x;
  int y;
  int z;
};

void neighbor_state_counts(struct vector3 sim_size, int thread, __global double4* cells){
  int cell;

  for(int z = -1; z <= 1; z++){
    for(int y = -1; y <= 1; y++){
      for(int x = -1; x <= 1; x++){
        cell = (thread + x + y*sim_size.y + z*(sim_size.y * sim_size.x));
        printf("%i", cell);
        printf("\n");
      }
    }
  }

}





void main(){
  struct vector3 sim_size;
  sim_size.x = 4;
  sim_size.y = 9;
  sim_size.z = 3;
  int thread = 57;

  neighbor_state_counts(sim_size, thread);

}









inline int neighbor_state_counts(uint4 sim_size, int thread){
  uint cell = 0;

  //uint ssx = sim_size.x;
  //uint ssy = sim_size.y;
  //uint ssz = sim_size.z;



  for(int z = -1; z <= 1; z++){
    for(int y = -1; y <= 1; y++){
      for(int x = -1; x <= 1; x++){
        cell += (thread + x + y *sim_size.y + z*(sim_size.y * sim_size.x));

        //cell += (thread + x + y * ssy + z*(ssy * ssx));
      }
    }
  }
  return cell;
}



//sim_size.x = 4;
//sim_size.y = 9;
//sim_size.z = 3;
//int thread = 57;
