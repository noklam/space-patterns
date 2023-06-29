"""
This is a boilerplate pipeline 'pipe2'
generated using Kedro 0.18.8
"""


def random_node2(dataset, parameter):
    print(parameter)
    _random_fn()
    return dataset

def _random_fn():
    print("I'm here!")