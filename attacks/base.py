from abc import ABCMeta

import torch

from advertorch.utils import replicate_input


class Attack(object):
    """
    Abstract base class for all attack classes.
    :param predict: forward pass function.
    :param loss_fn: loss function that takes .
    :param clip_min: mininum value per input dimension.
    :param clip_max: maximum value per input dimension.
    """

    __metaclass__ = ABCMeta

    def __init__(self, predict, loss_fn, clip_min, clip_max):
        """Create an Attack instance."""
        self.predict = predict
        self.loss_fn = loss_fn
        self.clip_min = clip_min
        self.clip_max = clip_max

    def perturb(self, x, **kwargs):
        """Virtual method for generating the adversarial examples.
        :param x: the model's input tensor.
        :param **kwargs: optional parameters used by child classes.
        :return: adversarial examples.
        """
        error = "Sub-classes must implement perturb."
        raise NotImplementedError(error)

    def __call__(self, *args, **kwargs):
        return self.perturb(*args, **kwargs)