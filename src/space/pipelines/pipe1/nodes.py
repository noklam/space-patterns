"""
This is a boilerplate pipeline 'pipe1'
generated using Kedro 0.18.8
"""
import logging
log = logging.getLogger(__name__)
def random_node(dataset, parameter):
    print(parameter)
    return dataset
