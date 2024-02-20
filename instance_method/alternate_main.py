## help to identify the Lineage of the class
import MathClasses

if __name__ == "__main__":
    simple_ops = MathClasses.SimpleOps()
    simple_ops.set_values(10, 5)
    print("Simple Operations:")
    print(simple_ops.add())
    print(simple_ops.sub())
    print(simple_ops.mul())
    print(simple_ops.divide())
    del simple_ops

    complex_ops = MathClasses.ComplexOps()
    complex_ops.set_value(16)
    print("\nComplex Operations:")
    print(complex_ops.sqrt())
    complex_ops.set_value(27)
    print(complex_ops.cubert())
    complex_ops.set_data([10, 12, 23, 23, 16])
    print(complex_ops.std_deviation())
    del complex_ops
