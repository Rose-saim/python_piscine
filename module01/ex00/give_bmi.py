def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
        raise(AssertionError('Height and weight have to be int or float'))
    elif type(height) != type(weight):
        print(AssertionError('Height and weight is not same variable'))
    bmi = [w / (h**2) for h, w in zip(height, weight)]
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int):
        raise(AssertionError('Limit is not int'))
    return list(map(lambda x: x > limit, bmi))

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()