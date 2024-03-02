from enum import Enum
from .components import COMPONENTS_REPOSITORY
from jsx.renderer import render_json


class WSRouterCommands(str, Enum):
    GET_COMPONENT = "component"


def get_component(name: str, props={}):
    cls = COMPONENTS_REPOSITORY.get_component(name)
    return "component", render_json(cls(**props))


ws_router = {WSRouterCommands.GET_COMPONENT: get_component}
