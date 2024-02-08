def str_obr(s: str, pd_s: str) -> int:
    """_summary_

    Args:
        s (str): liter
        pd_s (str): considered string

    Returns:
        int: count of liters
    """
    if len(s) != 1:
        raise ValueError("Lens of litter is not equal 1")
    m = 0
    count = 0
    for i in pd_s:
        if s == i:
            count += 1
        else:
            if count > m:
                m = count
            count = 0

    return m


if __name__ == "__main__":
    print(str_obr("a", "aaabam"))
