import math


class UserDistribution:

    def __init__(self, number, exponent_index, min_salary, max_salary):
        self.number = number
        self.exponent_index = exponent_index
        self.max_salary = max_salary
        self.min_salary = min_salary


        self.norm_coeff = (number * (1 - exponent_index) / self.max_salary) / (1 ** (1 - exponent_index) -
                                                             (self.min_salary / self.max_salary) ** (1 - exponent_index))
        # self.norm_coeff = (exponent_index * number) / (math.exp(-exponent_index * self.min_salary) -
        #                                                math.exp(-exponent_index * self.max_salary))

    def get(self, price):
        return round(self.norm_coeff * (price / self.max_salary) ** (-self.exponent_index))
        # return round(self.norm_coeff * math.exp(-self.exponent_index * price))

    def distrib(self, max_salary=None, price_step = 1):
        if max_salary is None or max_salary > self.max_salary:
            max_salary = self.max_salary
        def distrib_gen():
            for price in range(self.min_salary, max_salary, price_step):
                yield (price, self.get(price))
        return distrib_gen()

