from django.test import TestCase

# Create your tests here.

for x in range(1, 16):
    print("fizz"[x % 3 * 4:] + "buzz"[x % 5 * 4 :] or x)
