from typing import Optional
import math


class Complex:
    """Реализация комплексных чисел."""

    def __init__(self, real: Optional[float] = None, img: Optional[float] = None, r: Optional[float] = None, phi: Optional[float] = None):
        if real is not None and img is not None:
            self.real = real
            self.img = img
        elif r is not None and phi is not None:
            self.r = r
            self.phi = phi
        self.compute_other_form()

    def exp_form(self):
        return self.r, self.phi

    def algb_form(self):
        return self.real, self.img

    def compute_other_form(self):
        if "r" in self.__dict__.keys():
            r, phi = self.exp_form()
            self.real, self.img = r * math.cos(phi), r * math.sin(phi)
        elif "real" in self.__dict__.keys():
            real, img = self.algb_form()
            r = math.sqrt(real**2 + img**2)
            phi = math.acos(real / r)
            self.r, self.phi = r, phi

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if key in self.__dict__.keys():
            self[key] = value

    def __add__(self, other):
        real_1, img_1 = self.algb_form()
        if isinstance(other, Complex):
            real_2, img_2 = other.algb_form()
            return Complex(real_1 + real_2, img_1 + img_2)
        else:
            return Complex(real_1 + other, img_1)

    def __radd__(self, other):
        return Complex(other + self.real, self.img)

    def __sub__(self, other):
        real_1, img_1 = self.algb_form()
        if isinstance(other, Complex):
            real_2, img_2 = other.algb_form()
            return Complex(real_1 - real_2, img_1 - img_2)
        else:
            return Complex(real_1 - other, img_1)

    def __rsub__(self, other):
        return Complex(other - self.real, -self.img)

    def __mul__(self, other):
        if isinstance(other, Complex):
            r_1, phi_1 = self.exp_form()
            r_2, phi_2 = other.exp_form()
            return Complex(None, None, r_1 * r_2, phi_1 + phi_2)
        else:
            return Complex(self.real * other, self.img * other)

    def __rmul__(self, other):
        return Complex(self.real * other, self.img * other)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            r_1, phi_1 = self.exp_form()
            r_2, phi_2 = other.exp_form()
            return Complex(None, None, r_1 / r_2, phi_1 - phi_2)
        else:
            return Complex(self.real / other, self.img / other)

    def __rtruediv__(self, other):
        return Complex(other, 0) / self

    def __eq__(self, other):
        self_real, self_img = self.exp_form()
        other_real, other_img = other.exp_form()
        if self_real == other_real and self_img == other_img:
            return True
        else:
            return False

    def __str__(self):
        if self.img < 0:
            return f"{self.real}{self.img}*i"
        elif self.img == 0:
            return self.real
        else:
            return f"{self.real}+i*{self.img}"

    def __abs__(self):
        return self.r


if __name__ == "__main__":
    a = Complex(0.2, 8)
    b = Complex(r=4, phi=0.4)
    c = Complex(7, 9)
    print(a, b)
    print(a * b, a + b, a - c, a / c, sep="\n")
    print(
        1 / Complex(1, 2), 1 + Complex(1, 2),
        2 * Complex(1, 3), 4 - Complex(3, 4),
        sep="\n"
    )
