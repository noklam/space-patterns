"""
This is a boilerplate pipeline 'pipe1'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import random_node2


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=random_node2,
            inputs=["france_preprocessed_companies", "params:hello2"],
            outputs="france_final",
            name="second_france_node",
        ),
        node(
            func=random_node2,
            inputs=["germany_preprocessed_companies", "params:hello2"],
            outputs="germany_final",
            name="second_germany_node",
        ),
        node(
            func=random_node2,
            inputs=["switzerland_preprocessed_companies", "params:hello2"],
            outputs="switzerland_final",
            name="second_switzerland_node",
        ),
    ])
