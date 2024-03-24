'''
    testing importing the modules of the package
'''
import pytest
def test_fail_unexistent_module_import():
    import personalization_experiment
    fake_module = 'banana'
    assert hasattr(personalization_experiment, f'{fake_module}') == False 

def test_succeed_existent_dataset_module_import():
    import personalization_experiment
    assert hasattr(personalization_experiment, 'dataset') == True 
