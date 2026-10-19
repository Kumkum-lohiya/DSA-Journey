
import math


class Solution:
    def quadraticRoots(self, a, b, c):
        """
        Find the real roots of ax² + bx + c = 0.

        Returns:
            A list containing the floor values of both roots
            in descending order, or [-1] if roots are imaginary.
        """

        # Calculate the discriminant
        D = b**2 - 4 * a * c

        # No real roots
        if D < 0:
            return [-1]

        # Calculate both roots
        r1 = math.floor((-b + math.sqrt(D)) / (2 * a))
        r2 = math.floor((-b - math.sqrt(D)) / (2 * a))

        # Return roots in descending order
        return sorted([r1, r2], reverse=True)
