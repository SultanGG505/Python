"""3. Составить описание класса многочленов от одной переменной, задаваемых
степенью многочлена и массивом коэффициентов. Предусмотреть методы для
вычисления значения многочлена для заданного аргумента, операции сложения,
вычитания и умножения многочленов с получением нового объекта-многочлена,
вывод на экран описания многочлена.
"""


class Polynomial():
    def __init__(self, power: int, coefficients: list):
        try:
            if power <= 0:
                raise AttributeError
        except AttributeError:
            print("степень не может быть меньше нуля")
            quit()
        try:
            if power != len(coefficients) - 1:
                raise ValueError
        except ValueError:
            print("мало/много коэффицентов")
            quit()
        self.power = power
        self.coefficients = coefficients

    def __str__(self):
        power = self.power
        coeffs = self.coefficients.copy()
        view = ""
        for coeff in coeffs:
            if coeff != 0:
                if coeff > 0:
                    sign = " + "
                else:
                    sign = " - "
                if power != 0 and (coeff == 1 or coeff == -1):
                    coeff = ""
                coeff = str(coeff).strip('-')

                if power == 1:
                    add_string = coeff + 'x'
                elif power == 0:
                    add_string = coeff
                else:
                    add_string = coeff + "x^" + str(power)

                view = view + sign + add_string
            power -= 1
        view = view.lstrip(' +')
        return view

    def __add__(self, polynom_2):
        coeffs_1 = self.coefficients[:]
        coeffs_2 = polynom_2.coefficients[:]
        while len(coeffs_1) != len(coeffs_2):
            min(coeffs_1, coeffs_2, key=len).insert(0, 0)
        sum_coeffs = list(map(lambda coeff_1, coeff_2: coeff_1 + coeff_2,
                              coeffs_1, coeffs_2))
        sum_power = max(self.power, polynom_2.power)
        summ = Polynomial(sum_power, sum_coeffs)
        return summ

    def __sub__(self, polynom_2):
        coeffs_1 = self.coefficients[:]
        coeffs_2 = polynom_2.coefficients[:]
        while len(coeffs_1) != len(coeffs_2):
            min(coeffs_1, coeffs_2, key=len).insert(0, 0)
        diff_coeffs = list(map(lambda coeff_1, coeff_2: coeff_1 - coeff_2,
                               coeffs_1, coeffs_2))
        diff_power = max(self.power, polynom_2.power)
        difference = Polynomial(diff_power, diff_coeffs)
        return difference

    def __mul__(self, polynom_2):
        coeffs_1 = self.coefficients[:]
        coeffs_2 = polynom_2.coefficients[:]
        while len(coeffs_1) != len(coeffs_2):
            min(coeffs_1, coeffs_2, key=len).insert(0, 0)
        prod_power = (len(coeffs_1) - 1) * 2
        counter = 0
        prod_coeffs = [0 for i in range(prod_power + 1)]
        for coeff_1 in coeffs_1:
            iteration_coeffs = list(map(lambda coeff_2: coeff_1 * coeff_2, coeffs_2))
            for i in range(counter):
                iteration_coeffs.insert(0, 0)
            while len(iteration_coeffs) != prod_power + 1:
                iteration_coeffs.append(0)
            prod_coeffs = list(
                map(lambda iter_coeff, prod_coeff: iter_coeff + prod_coeff, iteration_coeffs, prod_coeffs))
            counter += 1
        product = Polynomial(prod_power, prod_coeffs)
        return product

    def calculate(self, x):
        answer = 0
        power = self.power
        for coeff in self.coefficients:
            answer = answer + (coeff * (x ** power))
            power -= 1
        return answer


first_poly = input("Введите степень и коэффициенты 1ого многочлена через пробел:")
try:
    power_1 = int(first_poly.split(' ')[0])
    coefficients_1 = list(map(int, first_poly.split(' ')[1:]))
except ValueError:
    print("Ошибка ввода")
    quit()
first_poly = Polynomial(power_1, coefficients_1)
print(first_poly)

second_poly = input("Введите степень и коэффициенты 2ого многочлена через пробел:")
try:
    power_2 = int(second_poly.split(' ')[0])
    coefficients_2 = list(map(int, second_poly.split(' ')[1:]))
except ValueError:
    print("Ошибка ввода")
    quit()
second_poly = Polynomial(power_2, coefficients_2)
print(second_poly)

summ = first_poly + second_poly
print('Сумма многочленов равна: {}'.format(summ))
difference = first_poly - second_poly
print('Разность многочленов равна: {}'.format(difference))
product = first_poly * second_poly
print('Произведение многочленов равно: {}'.format(product))
x = int(input("введите x "))
y = first_poly.calculate(x)
print('При x =', x, '1ый многочлен равен: {}'.format(y))
