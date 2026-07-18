def ft_map(function_to_apply, iterable):
    """ Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking a iterable.
        iterable: an iterable object (list, tuple, iterator)
    Return:
        An iterable.
        None if the iterable can not be used by the function
    """
    try:
        try:
            for el in iterable:
                yield function_to_apply(el)
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
            return None
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
