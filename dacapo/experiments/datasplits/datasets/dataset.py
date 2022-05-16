from .arrays import Array

from abc import ABC, abstractmethod
from typing import Optional


class Dataset(ABC):
    raw: Array
    gt: Optional[Array] = None
    mask: Optional[Array] = None

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Dataset({self.name})"

    def __str__(self):
        return f"Dataset({self.name})"

    def _neuroglancer_layers(self, prefix="", exclude_layers=None):
        layers = {}
        exclude_layers = exclude_layers if exclude_layers is not None else set()
        if (
            self.raw._can_neuroglance()
            and not self.raw._source_name() in exclude_layers
        ):
            layers[self.raw._source_name()] = self.raw._neuroglancer_layer()
        if (
            self.gt is not None
            and self.gt._can_neuroglance()
            and not self.gt._source_name() in exclude_layers
        ):
            layers[self.gt._source_name()] = self.gt._neuroglancer_layer()
        if (
            self.mask is not None
            and self.mask._can_neuroglance()
            and not self.mask._source_name() in exclude_layers
        ):
            layers[self.mask._source_name()] = self.mask._neuroglancer_layer()
        return layers
