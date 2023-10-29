import numpy as np
def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list) or isinstance((start, end), int):
        raise(AssertionError('Parameter is not conform'))
    np_family = np.array(family)
    print(f"My shape is : {np.shape(np_family)}")
    B = np_family[start:end]
    print(f"My new shape is : {np.shape(B)}")
    return B.tolist()

def main():
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()