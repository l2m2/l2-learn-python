from functools import partial

def impartial(x, y, z):
    return x + y + z

partial_fn_2 = partial(impartial, 2)
print(partial_fn_2(3, 4))

partial_fn_2_3 = partial(impartial, 2, 3)
print(partial_fn_2_3(4))

partial_fn_null = partial(impartial)
print(impartial(2, 3, 4))