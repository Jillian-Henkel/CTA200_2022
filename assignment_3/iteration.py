import numpy as np

# constants:
Z0=0 + 0j  
n_its = 100  # number of iterations to use in the z_i equation iteration

def iteration(c, z0=Z0, niters=n_its):
    """
    iteration(c, z0=Z0, niters=n_its):
    
    Produces the iteration at which z_i diverges for z_(i + 1) = z_i + c for a given staring condition.
    Returns -1 in the case that z_i does not diverge.

    Parameters:
    ---------
    c: complex
    Number in complex plane.
    z0 = Z0: complex, default
    The initial condition for the quadratic map is z0, and it is set to 0 by default.
    
    Returns:
    ---------
    i: int
    The number of iterations required for the quadratic map to diverge.

    """
    zi = np.array([z0] * niters)  
    
    for i in range(1, niters):  
        zi[i] = (zi[i - 1] ** 2) + c  
        if np.abs(zi[i].real) > 2. or np.abs(zi[i].imag) > 2.:  # comparing zi to zi-1
            return i  
    return -1  # -1 will respresent convergence.
