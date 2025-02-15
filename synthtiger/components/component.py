"""
SynthTIGER
Copyright (c) 2021-present NAVER Corp.
MIT license
"""

from abc import ABC, abstractmethod
from typing_extensions import Any, Dict


class Component(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def sample(self, meta=None) -> Dict[str, Any]:
        pass

    def apply(self, layers, meta=None) -> Dict[str, Any]:
        raise AttributeError

    def data(self, meta) -> Dict[str, Any]:
        raise AttributeError

    def _init(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
