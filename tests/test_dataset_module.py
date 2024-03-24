'''
    testing the dataset module
'''
import pytest
def test_succeed_create_dataset():
    from personalization_experiment import dataset
    dataset.create('some_file_path')
    assert False == True
