#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    quotient = None
    for n in range(list_length):
        try:
            quotient = (my_list_1[n] / my_list_2[n])
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result.append(quotient)
    return result
