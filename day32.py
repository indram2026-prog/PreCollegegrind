"""
================================================================================
          STANDALONE DESCRIPTIVE STATISTICS CALCULATOR (NO DEPENDENCIES)
================================================================================

ABOUT:
This is a purely standalone Python script designed to compute Mean, Median, and 
Mode manually from core Python algorithms without using any internal or external 
libraries (no `statistics`, `math`, `numpy`, or `pandas`).

GITHUB READY:
This file contains the core algorithms, test benches, and a runtime CLI tool 
in a single self-contained script.

QUICK START:
    $ python stat_calculator.py
"""

# ==============================================================================
# 1. CORE STATISTICAL UTILITIES
# ==============================================================================

def calculate_mean(numbers):
    """Calculates the arithmetic average of a dataset."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """Calculates the middle point value of an ordered dataset."""
    if not numbers:
        return 0
    
    # Sort dataset in ascending order safely
    sorted_data = sorted(numbers)
    length = len(sorted_data)
    mid_index = length // 2
    
    # Handle even-length lists (average middle two) vs odd-length lists
    if length % 2 == 0:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    else:
        return sorted_data[mid_index]


def calculate_mode(numbers):
    """Calculates all most-frequent items. Handles multimodal or no-mode sets."""
    if not numbers:
        return []
    
    # Generate frequency map manually
    frequency_map = {}
    for value in numbers:
        frequency_map[value] = frequency_map.get(value, 0) + 1
        
    highest_frequency = max(frequency_map.values())
    
    # If all items appear exactly once, no statistical mode exists
    if highest_frequency == 1 and len(numbers) > 1:
        return []
        
    # Gather items matching maximum occurrence criteria
    modes = [item for item, freq in frequency_map.items() if freq == highest_frequency]
    return sorted(modes)


# ==============================================================================
# 2. ISOLATED TEST HARNESS
# ==============================================================================

def run_automated_tests():
    """Runs automated unit assertions to guarantee algorithm validity."""
    print("[*] Launching Automated Testing Engine...")
    
    # Test Suite 1: Standard odd set
    odd_set = [9, 3, 1, 8, 3, 6, 7]
    assert round(calculate_mean(odd_set), 2) == 5.29, "Mean test failed (Odd Set)"
    assert calculate_median(odd_set) == 6, "Median test failed (Odd Set)"
    assert calculate_mode(odd_set) == [3], "Mode test failed (Odd Set)"
    
    # Test Suite 2: Balanced even set (bimodal properties)
    even_set = [10, 40, 20, 40, 20, 50, 60, 30]
    assert calculate_mean(even_set) == 33.75, "Mean test failed (Even Set)"
    assert calculate_median(even_set) == 35.0, "Median test failed (Even Set)"
    assert calculate_mode(even_set) == [20, 40], "Mode test failed (Even Set)"
    
    # Test Suite 3: Dataset possessing zero modal frequency
    unique_set = [1, 2, 3, 4, 5]
    assert calculate_mode(unique_set) == [], "Mode test failed (No Mode Set)"
    
    print("[+] All assertions passed successfully! Algorithms are structurally secure.\n")


# ==============================================================================
# 3. INTERACTIVE COMMAND LINE INTERFACE
# ==============================================================================

def interactive_session():
    """Provides a runtime environment for typing custom evaluation vectors."""
    print("=" * 60)
    print("       MANUAL STATISTICS ENGINE (MEAN, MEDIAN, MODE)")
    print("=" * 60)
    print("Instructions: Enter digits separated by spaces (e.g., 4 1 7 3 3 9)")
    
    user_string = input("\nEnter your dataset points: ").strip()
    if not user_string:
        print("[-] Data stream empty. Exiting execution context.")
        return

    try:
        # Convert user string cleanly to float array
        dataset = [float(element) for element in user_string.split()]
        
        # Display operational summaries
        print("\n" + "-"*40)
        print(f"Target Array : {dataset}")
        print(f"Sorted Array : {sorted(dataset)}")
        print("-"*40)
        print(f"Calculated Mean   : {calculate_mean(dataset):.4f}")
        print(f"Calculated Median : {calculate_median(dataset)}")
        print(f"Calculated Mode   : {calculate_mode(dataset)}")
        print("-"*40 + "\n")
        
    except ValueError:
        print("\n[!] Parsing Error: Input must contain numbers only.")


if __name__ == "__main__":
    # Execute structural tests instantly upon execution
    run_automated_tests()
    
    # Spin up interactive prompt engine
    interactive_session()