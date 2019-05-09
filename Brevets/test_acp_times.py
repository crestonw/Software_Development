'''
Nose tests for acp_times.py
'''

import acp_times
import arrow
import nose
import logging

def test_zero():
    '''
    Tests for control_dist_km equal to zero
    ''' 

    result = arrow.now().shift(hours=-3)
    assert close_time(0, 200, arrow.now()) == result.isoformat()
    assert open_time(0, 200, arrow.now()) == arrow.now().isoformat()
    
def test_norm():
    '''
    Tests for standard input
    '''

    result = arrow.now().shift(hours=4, minutes=0)
    assert close_time(120, 200, arrow.now()) == result.isoformat()

    result = arrow.now().shift(hours=-1, minutes=32)
    assert open_time(120, 200, arrow.now()) == result.isoformat()

def test_200():
    '''
    Test to see if the max close time of a 200 brevet is 13H30M
    '''

    result = arrow.now().shift(hours=9, minutes=30)
    assert close_time(200, 200, arrow.now()) == result.isoformat()

def test_over():
    '''
    Test to see if the max close time is held at the brevet distance and doesn't exceed that.
    '''

    result = arrow.now().shift(hours=9, minutes=30)
    assert close_time(205, 200, arrow.now()) == result.isoformat()

def test_no_hours():
    '''
    Tests to see if proper result if close and start should be under an hour.
    '''

    result = arrow.now().shift(hours=-4, minutes=18)
    assert open_time(10, 200, arrow.now()) == result.isoformat()

    result = arrow.now().shift(hours=-4, minutes=40)
    assert close_time(10, 200, arrow.now()) == result.isoformat()
    
