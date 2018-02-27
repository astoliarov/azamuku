# coding: utf-8


# https://stackoverflow.com/questions/16826400/how-do-i-write-a-nose2-plugin-that-separates-different-types-of-tests
# Revert feature from nose
def attr(*args, **kwargs):
    """Decorator that adds attributes to classes or functions
    for use with the Attribute (-a) plugin.
    """
    def wrap_ob(ob):
        for name in args:
            setattr(ob, name, True)
        for name, value in kwargs.items():
            setattr(ob, name, value)
        return ob
    return wrap_ob

