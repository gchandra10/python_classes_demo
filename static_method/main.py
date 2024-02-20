## Method 1: Split the Classes into multiple files.
from SimpleOperations import *
from ComplexOperations import *

## Alternate way to keep all classes in a single file.
## from MathClasses import SimpleOperations, ComplexOperations

if __name__ == "__main__":
    # Simple Operations
    print("Simple Operations:")
    print(SimpleOperations.add(10, 5))
    print(SimpleOperations.sub(10, 5))
    print(SimpleOperations.mul(10, 5))
    print(SimpleOperations.divide(10, 5))

    # Complex Operations
    print("\nComplex Operations:")
    print(ComplexOperations.sqrt(16))
    print(ComplexOperations.cubert(27))
    print(ComplexOperations.std_deviation([10, 12, 23, 23, 16]))
