"""
Collection of the core mathematical operators used throughout the code base.
"""


import math
from typing import List

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    return x * y


def id(x):
    ":math:`f(x) = x`"
    return x


def add(x, y):
    ":math:`f(x, y) = x + y`"
    return x + y


def neg(x):
    ":math:`f(x) = -x`"
    return -x


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    return 1 if x < y else 0


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    return 1 if x == y else 0


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    return x if x > y else y


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2`"
    return abs(x - y) < 1e-2


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    else:
        return math.exp(x) / (1 + math.exp(x))


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    return x if x >= 0 else 0


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    r"If :math:`f = log` as above, compute :math:`d \times f'(x)`"
    
    return mul(d, 1 / x)


def inv(x):
    ":math:`f(x) = 1/x`"
    return 1 / x


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute :math:`d \times f'(x)`"
    return mul(d, mul(-2, inv(-x)))


def relu_back(x, d):
    r"If :math:`f = relu` compute :math:`d \times f'(x)`"
    return mul(d, lt(0, x))


# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """

    def apply(L : List):
        new_l = [fn(l) for l in L]
        return new_l

    return apply

def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    
    map_ = map(neg)
    new_list = map_(ls)
    return new_list


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """
    
    def apply_fn(l1 , l2):
        new_l = [fn(x , y) for x , y in zip(l1,l2)]
        return new_l
    return apply_fn


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"

    adding_map = zipWith(add)
    return adding_map(ls1 , ls2)

def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """

    def apply_fn(ls):
        f = ls[start]
        for i in range(start,len(ls)-1):
            f = fn(f,ls[i+1])
        return f
    return apply_fn
        


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."

    if len(ls) == 0 :
        return 0
    if len(ls) == 1:
        return ls[0]
    reduce_sum = reduce(add ,0)
    return reduce_sum(ls)

def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    if len(ls) == 0 :
        return 0
    if len(ls) == 1:
        return ls[0]
    reduce_prod = reduce(mul,0)
    return reduce_prod(ls)