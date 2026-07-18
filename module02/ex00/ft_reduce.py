def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    try:
        try:
            iters = iter(iterable)
            cum = function_to_apply(next(iters), next(iters))
            el = next(iters, None)
            while el:
                cum = function_to_apply(cum, el)
                el = next(iters, None)
            return cum
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
