from sum_numbers import sum_to_n_for, sum_to_n_while, sum_to_n_formula, time_function


def verify_implementations() -> None:
    """Test all implementations with various inputs and verify they give same results."""
    test_cases = [0, 1, 5, 10, 100, 1000]
    implementations = [
        ('For Loop', sum_to_n_for),
        ('While Loop', sum_to_n_while),
        ('Formula', sum_to_n_formula)
    ]
    
    print("Verification Tests:")
    print("-" * 40)
    
    for n in test_cases:
        print(f"\nTesting n = {n}")
        results = []
        for name, func in implementations:
            result = func(n)
            results.append(result)
            print(f"{name:12}: {result}")
        
        # Verify all implementations give same result
        assert all(r == results[0] for r in results), f"Inconsistent results for n = {n}"


def benchmark_implementations() -> None:
    """Compare performance of different implementations."""
    test_sizes = [100, 1000, 10000, 100000]
    implementations = [
        ('For Loop', sum_to_n_for),
        ('While Loop', sum_to_n_while),
        ('Formula', sum_to_n_formula)
    ]
    
    print("\nPerformance Benchmarks:")
    print("-" * 40)
    print(f"{'n':>10} {'For Loop':>12} {'While Loop':>12} {'Formula':>12}")
    print("-" * 50)
    
    for n in test_sizes:
        times = []
        for _, func in implementations:
            avg_time = time_function(func, n)
            times.append(avg_time)
        
        print(f"{n:10d} {times[0]:12.3f} {times[1]:12.3f} {times[2]:12.3f} ms")


def test_error_handling() -> None:
    """Test error handling for negative inputs."""
    print("\nError Handling Tests:")
    print("-" * 40)
    
    implementations = [
        ('For Loop', sum_to_n_for),
        ('While Loop', sum_to_n_while),
        ('Formula', sum_to_n_formula)
    ]
    
    for name, func in implementations:
        try:
            func(-1)
            print(f"{name}: Failed - did not raise ValueError")
        except ValueError as e:
            print(f"{name}: Passed - correctly raised ValueError: {e}")


def main() -> None:
    verify_implementations()
    benchmark_implementations()
    test_error_handling()


if __name__ == "__main__":
    main()