#!/usr/bin/env python3

import pytest
import example

def test_average():
    assert example.average([3, 5]) == 4

def test_average_empty_list():
    assert example.average([]) == 0
