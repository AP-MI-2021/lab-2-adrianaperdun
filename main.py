def get_largest_prime_below(n):
    """
    Functia returneaza ultimul numar prim mai mic decat n
    :param n: n, k, ok, i
    :return: returneaza in k ultimul numar prim
    """
    k = 0
    while k == 0:
        ok = True
        n = n - 1
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                ok = False
        if ok:
            k = n
    return k


def test_get_largest_prime_below():
    assert (get_largest_prime_below(6)) == 5
    assert (get_largest_prime_below(10)) == 7

def is_palindrome(n) -> bool:

    inv = 0
    x = n
    while (x != 0):
        inv = inv * 10
        inv = inv + (x % 10)
        x = x // 10
    if (inv == n):
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(23432) == True
    assert is_palindrome(123) == False


def get_age_in_days(birthday):
    """
    Functia returneaza varsta unei persoane in zile
    :param birthday: m(ziua), p(luna), q(anul), zile_total, montn[]
    :return: returneaza in zile_total numarul total de zile
    """
    m = int(birthday[0:2])
    p = int(birthday[3:5])
    q = int(birthday[6:10])
    zile_total = 0
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, p):
        zile_total = zile_total - month[i]
    zile_total = zile_total - m
    zile_total = zile_total - q * 365
    zile_total = zile_total + 4
    zile_total = zile_total + 2021 * 365
    for i in range(0, 10):
        zile_total = zile_total + month[i]
    for i in range(q, 2021):
        if i % 4 == 0:
            zile_total = zile_total + 1
    return zile_total


def main():
    while True:
        print("1. Gaseste ultimul numar prim, mai mic decat cel dat.")
        print("2. Calculeaza varsta unei persoane in zile.")
        print("3. Palidrom.")
        print("x.Iesire")
        optiune = input("Dati optiunea:")
        if optiune == 'x':
            break
        elif optiune == '1':
            nr = int(input("Dati numarul:"))
            if nr < 3:
                print("Nu este o valoare valida.Reincercati.")
            else:
                maxnr = get_largest_prime_below(nr)
                print(f"Ultimul numar prim mai mic decat {nr} este: {maxnr}")
        elif optiune == '2':
            birthday = input("Introduceti data nasterii (DD<MM/YYYY): ")
            print(get_age_in_days(birthday))
        elif optiune == '3':
            n = int(input("Introduceti n="))
            print(is_palindrome(n))
        else:
            print("Optiune gresita. Reincercati.")

    test_get_largest_prime_below()


main()
