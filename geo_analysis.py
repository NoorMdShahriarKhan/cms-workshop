#This is my geometry analysis
"""
Functions and script for geometry analysis.
"""

import os
import numpy
import sys




def calculate_distance(atomA,atomB):
    """
    calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list
        A list of cooedinates [x,y,z]
    atom2: list
        A list of coordinates [x,y,z]

    Return
    ------
    bond_length: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0,0,0],[0,0,1])
    1.0
    """
    x_distance = atomA[0]-atomB[0]
    y_distance = atomA[1]-atomB[1]
    z_distance = atomA[2]-atomB[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(bond_distance,minimum_value=0,maximum_value=2.0):
    """
    Check if distance is a bond

    Parameters
    ----------
    bond_distance: float
        The distance between atoms
    minimum_value: float
        minimum value of the atom distance
    maximum_value: float
        maximum value of the atom distance
    Returns
    -------
    true if bond
    False if not a bond

    """

#CHeck that atom distance is a float.
    if not isinstance(bond_distance, float):
        raise TypeError(F'bond_distance must be type float. {bond_distance}')


    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False
if __name__=="__main__":  #to import file
    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file')

    file_location = sys.argv[1]
    #file_location = os.path.join('data','benzene.xyz')
    xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')

    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(float)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB < numA:
                distance_AB = calculate_distance(atomA, atomB)
                if bond_check(distance_AB) is True:
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB:.3f}')
