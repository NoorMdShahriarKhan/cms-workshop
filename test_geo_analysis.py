"""
Test for geom_analysis.py
"""
import geo_analysis as ga

def test_calculate_distance():
    coord1 = [0,0,2]
    coord2 = [0,0,0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2.0

#conda install pytest-cov
