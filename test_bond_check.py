"""
Test for bond_check.py
"""
import geo_analysis as ga
import pytest

def test_bond_check_f():
    bond_length= 3.0

    observed = ga.bond_check(bond_length)

    assert  observed == False

def test_bond_check_t():
    bond_length= 1.9

    observed = ga.bond_check(bond_length)

    assert  observed == True
#conda install pytest-cov

def test_bond_check_error():
    bond_distance ='a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_distance)
