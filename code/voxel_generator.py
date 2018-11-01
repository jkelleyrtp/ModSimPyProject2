import numpy as np
import pyopencl as cl



class simulation:
    def __init__(self, size = (10,10,10) ):
        self.simulation_size = size

    def load_update_func_from_file(self, file_name):
        f = open(filename, 'r')
        self.program_text = "".join(f.readlines())

        pass

    def load_update_func_from_text(self,kernel_code):
        f = kernel_code
        fstr = "".join(f.readlines())
        self.program_text = "".join(f.readlines())
        pass


    def run_simulation(self, device_id = -1):
        COMPUTE = _COMPUTE_ENGINE(self.program_text, device_id);
        results = COMPUTE.EXECUTE(self.system, self.state)

        pass

    def _COMPUTE_ENGINE:
        def __init__(self, program_text, device_id):
            # Setup OpenCL platformw
            platform = cl.get_platforms()
            computes = [platform[0].get_devices()[device_id]]
            print "New context created on", computes
            self.ctx = cl.Context(devices=computes)
            self.queue = cl.CommandQueue(self.ctx)
            self.mf = cl.mem_flags

            # Open and build cl code
            self.program = cl.Program(self.ctx, program_text).build()

        def EXECUTE(self, system, state):

            for step in
            self.program.execute(self.queue, num_kernels, None, *(kernelargs))
