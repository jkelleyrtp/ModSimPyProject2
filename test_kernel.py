#import code.compute as COMPUTE
import numpy as np
import pyopencl as cl


platform = cl.get_platforms()
computes = [platform[0].get_devices()[2]]
print("New context created on {}".format(computes))
ctx = cl.Context(devices=computes)
queue = cl.CommandQueue(ctx)
mf = cl.mem_flags

# Open and build cl code
f = open("kernels/voxel-virus2.cl", 'r')
program_text = "".join(f.readlines())
program = cl.Program(ctx, program_text).build()

#program.execute(queue, num_kernels, None, *(kernelargs))


#array_size = (100,100,10)
array_size = [5,5,5]

positions = np.ones(array_size).astype(np.uint32)
results = np.zeros(array_size).astype(np.uint32)


p_buf = cl.Buffer(ctx,  mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=positions ) # Positions
r_buf = cl.Buffer(ctx,  mf.READ_WRITE, results.nbytes)

queue.finish()


kernelargs = (p_buf, r_buf, np.array(array_size + [0], dtype = np.uint32))

print('started')
for t in range(25000):
    program.compute_interaction(queue, (positions.size,), None, *(kernelargs))

print("computed")

queue.finish()

ret_val = np.empty_like(results).astype(np.int32)


read = cl.enqueue_copy(queue, ret_val, r_buf)
queue.finish()
read.wait()
r_buf.release()
print(ret_val)
