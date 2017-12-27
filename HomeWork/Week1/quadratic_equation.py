import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def find_root():
    # Assumption. All input coefs such that equation has exact 2 roots.
    root1 = (-b-(b**2-4.*a*c)**0.5)/(2.*a)
    root2 = (-b+(b**2-4.*a*c)**0.5)/(2.*a)
    return int(root1), int(root2)

print("\n".join(list(map(str, find_root()))))
