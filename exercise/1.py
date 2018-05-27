# -*- coding: utf-8 -*-

'''
数值的整数次方

实现函数`double Power(double base, int exponent)`，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

@author: happyin3
@created: 2018.05.27
'''


def power_cus(base, exponent):
    '''
    数值的整数次方

    :param base: <float> 数值
    :param exponent: <int> 整数次方
    :return: <float>
    '''
    assert isinstance(exponent, int) is True

    if base == 0 and exponent != 0:
        return 0.0

    if exponent == 0:
        return 1.0

    sign_flag = True if exponent > 0 else False

    result = 1
    for i in xrange(abs(exponent)):
        result *= base

    if not sign_flag:
        return 1.0 / result
    return result

if __name__ == '__main__':
    assert power_cus(0, 0) == 1.0
    assert power_cus(0, 2) == 0.0
    assert power_cus(2, 2) == 4
    print power_cus(2, -2)
    assert power_cus(2, -2) == 0.25
    power_cus(0, 0.5)
