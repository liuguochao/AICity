from __future__ import absolute_import

from .resnet import *
from .multi_attribute_3 import *
from .cross_entropy_trihard import *
from .cross_trihard_senet import *
from .cross_trihard_se_resnet import *
from .direction import *


__factory = {
    'multi_attribute_3_resnet50':multi_attribute_3_resnet50,
    'cross_entropy_trihard_resnet101':cross_entropy_trihard_resnet101,
    'cross_trihard_senet101':cross_trihard_senet101,
    'cross_trihard_se_resnet152':cross_trihard_se_resnet152,
    'direction_resnet50':direction_resnet50,
}


def names():
    return sorted(__factory.keys())


def create(name, *args, **kwargs):
    """
    Create a model instance.

    Parameters
    ----------
    name : str
        Model name. Can be one of 'inception', 'resnet18', 'resnet34',
        'resnet50', 'resnet101', and 'resnet152'.
    pretrained : bool, optional
        Only applied for 'resnet*' models. If True, will use ImageNet pretrained
        model. Default: True
    cut_at_pooling : bool, optional
        If True, will cut the model before the last global pooling layer and
        ignore the remaining kwargs. Default: False
    num_features : int, optional
        If positive, will append a Linear layer after the global pooling layer,
        with this number of output units, followed by a BatchNorm layer.
        Otherwise these layers will not be appended. Default: 256 for
        'inception', 0 for 'resnet*'
    norm : bool, optional
        If True, will normalize the feature to be unit L2-norm for each sample.
        Otherwise will append a ReLU layer after the above Linear layer if
        num_features > 0. Default: False
    dropout : float, optional
        If positive, will append a Dropout layer with this dropout rate.
        Default: 0
    num_classes : int, optional
        If positive, will append a Linear layer at the end as the classifier
        with this number of output units. Default: 0
    """
    if name not in __factory:
        raise KeyError("Unknown model:", name)
    return __factory[name](*args, **kwargs)