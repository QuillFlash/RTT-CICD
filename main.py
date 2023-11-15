""" Mádosfokú egyenlet megoldása pythonban"""
import math


class EgyenletMegoldo():
    """ egyenlet megoldó osztály"""
    def masodfoku_egyenlet_megoldo(self, var_a, var_b, var_c):
        """ másodfokú egyenlet megoldó metódus"""

        if type(var_a) not in [int, float] or type(var_b) not in [int, float] or type(var_c) not in [int, float]:
            raise TypeError('Csak int vagy float típus elfogadható!')

        d = math.pow(var_b, 2) - (4 * var_a * var_c)

        if d < 0:
            return None, None

        return (-var_b + math.sqrt(d)) / (2 * var_a), (-var_b - math.sqrt(d)) / (2 * var_a)

    def feladat_megoldo(self, var_a, var_b, var_c):
        """feladatmegoldó, mai a másodfokú egyenlet megoldó eredményét írja ki"""
        e = EgyenletMegoldo()
        x1, x2 = e.masodfokuEgyenletMegoldo(var_a, var_b, var_c )

        print(f"{var_a}x^2 + {var_b}x + {var_c} = 0")

        if (x1 is None) and (x2 is None):
            print("Nincs megoldás")
        elif x1 == x2:
            print(f"Egy megoldás van: {x1}")
        else:
            print(f"Két megoldás van: x1={x1}, x2={x2}")

#e = egyenletMegoldo()
#e.feladatMegoldo(1, 2, 8)
#e.feladatMegoldo(1, -14, 49)
#e.feladatMegoldo(1, 6, 8)
#e.feladatMegoldo("alma", 1, "körte")
