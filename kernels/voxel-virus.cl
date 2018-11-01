#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif


__kernel void compute_interaction(
	__global double4* cells,			//xyz, charge/mass

	 ){
	unsigned int thread = get_global_id(0);

	double4 cell = cells[thread];

  for(int offset = -12; offset< 27; offset++){
    print(offset);

  }







	double4 k1, k2, k3, k4, l1, l2, l3, l4;

	for(int iter = 0; iter<(num_steps); iter++){

		for (unsigned int sub_int = 0; sub_int < iter_nth; sub_int++){

			//Runge Kutta 4th Order

			k1 = dt * get_accel(pos, velo, local_coils, num_coils, c_sphere, ee_tab, ek_tab);
			l1 = dt * velo;

			k2 = dt * get_accel(  (pos + (0.5f * l1)), velo, local_coils, num_coils, c_sphere, ee_tab, ek_tab);
			l2 = dt * (velo + (0.5f * k1));

			k3 = dt * get_accel( (pos + (0.5f * l2)), velo, local_coils, num_coils, c_sphere, ee_tab, ek_tab);
			l3 = dt * (velo + (0.5f * k2));

			k4 = dt * get_accel( (pos + l3), velo, local_coils, num_coils, c_sphere, ee_tab, ek_tab);
			l4 = dt * (velo + k3);

			velo += (k1 + (2.0f*k2) + (2.0f*k3) +k4)/6.0f;
			pos += (l1 + (2.0f*l2) + (2.0f*l3) +l4)/6.0f;

      /*
      Euler's Method
			accel = get_accel(pos, velo, local_coils, num_coils, c_sphere, ee_tab, ek_tab); //returns acceleration
			velo += (accel * dt);
			pos += (velo * dt);
      */
		}
		dest[thread*num_steps + iter] = (float4)(pos.x, pos.y, pos.z, accel.w);
	}
}

/*
Device Info:

1 gb Max Global Memory
32 kbytes local memory
64 kbytes constant memory
6 compute units
657 MHz
float4s favored

*/
