import unittest

import exercise.reinforcement as reinforcement


class TestReinforcement(unittest.TestCase):
    # R-2.4
    def test_four(self):
        flower = reinforcement.Flower("rose", 10, 12.34)

        # test get
        self.assertEqual(flower.get_name(), "rose")
        self.assertEqual(flower.get_petals(), 10)
        self.assertEqual(flower.get_price(), 12.34)

        # test change value
        flower.set_name("flower")
        self.assertEqual(flower.get_name(), "flower")
        flower.set_petals(4)
        self.assertEqual(flower.get_petals(), 4)
        flower.set_price(10.0)
        self.assertEqual(flower.get_price(), 10.0)

    # R-2.9 - R-2.15
    def test_vector(self):
        # define vector instance
        v = reinforcement.Vector(5)
        v[1] = 23
        v[-1] = 45

        # R-2.9
        u = v - v
        self.assertEqual(u, reinforcement.Vector(5))

        # R-2.10
        a = -v

        b = reinforcement.Vector(5)
        b[1] = -23
        b[-1] = -45

        self.assertEqual(a, b)

        # R-2.11

        c = v + [1, 1, 1, 1, 1]
        d = [1, 1, 1, 1, 1] + v

        self.assertEqual(c, d)

        # R-2.12
        e = reinforcement.Vector(5)
        e[1] = 46
        e[-1] = 90

        f = v * 2
        self.assertEqual(e, f)

        # R-2.13
        g = 2 * v
        self.assertEqual(f, g)

        # R-2.14
        h = reinforcement.Vector(5)
        h[1] = 2
        i = reinforcement.Vector(5)
        i[1] = 4
        self.assertEqual(h * i, 8)

        # R-2.15
        j = reinforcement.Vector([1, 2])
        k = reinforcement.Vector(2)
        k[0] = 1
        k[-1] = 2
        self.assertEqual(j, k)


if __name__ == "__main__":
    unittest.main()
