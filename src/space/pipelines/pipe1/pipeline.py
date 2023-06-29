"""
This is a boilerplate pipeline 'pipe1'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import random_node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=random_node,
            inputs=["france_companies", "params:hello"],
            outputs="france_preprocessed_companies",
            name="france_node",
        ),
        node(
            func=random_node,
            inputs=["germany_companies", "params:hello"],
            outputs="germany_preprocessed_companies",
            name="germany_node",
        ),
        node(
            func=random_node,
            inputs=["switzerland_companies", "params:hello"],
            outputs="switzerland_preprocessed_companies",
            name="switzerland_node",
        ),
    ])
