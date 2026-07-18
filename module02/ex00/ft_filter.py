def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        if function_to_apply is None:
            def function_to_apply(x):
                return x == 0 or x == "" or x is False or x is None
        try:
            for el in iterable:
                if function_to_apply(el):
                    yield el
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
            return None
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
