def solution(money):
    if money >= 5500 :
        coffee = money // 5500
        return [coffee, money - (5500 * coffee)]
    return [0,money]