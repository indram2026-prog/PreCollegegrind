import unittest

def classify_blood_pressure(systolic: int, diastolic: int) -> str:
    """
    Classifies blood pressure based on hardcoded medical thresholds.
    Includes comprehensive data type and range validation.
    """
    # 1. Type Validation
    if not isinstance(systolic, (int, float)) or not isinstance(diastolic, (int, float)):
        raise TypeError("Inputs must be numeric integers or floats.")

    # 2. Medically Impossible Value Validation
    if systolic <= 40 or systolic >= 300:
        raise ValueError(f"Invalid Systolic value ({systolic}). Must be between 40 and 300 mmHg.")
    if diastolic <= 20 or diastolic >= 200:
        raise ValueError(f"Invalid Diastolic value ({diastolic}). Must be between 20 and 200 mmHg.")

    # 3. Core Classification Hierarchy
    if systolic > 180 or diastolic > 120:
        return "🚨 Hypertensive Crisis"
    elif systolic >= 140 or diastolic >= 90:
        return "🔴 Hypertension Stage 2"
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "🟡 Hypertension Stage 1"
    elif (120 <= systolic <= 129) and diastolic < 80:
        return "🟠 Elevated Blood Pressure"
    elif systolic < 120 and diastolic < 80:
        return "🟢 Normal Blood Pressure"
    else:
        return "⚠️ Mixed Reading"


# ==========================================
# 🧪 PROFESSIONAL AUTOMATED TEST SUITE
# ==========================================
class TestBloodPressureClassifier(unittest.TestCase):
    """
    Production-grade test suite using Python's native unittest framework.
    Each test function runs completely isolated.
    """
    
    def test_valid_classifications(self):
        """Verifies that correct medical classifications are returned for valid inputs."""
        test_cases = [
            (115, 75, "🟢 Normal Blood Pressure"),
            (125, 78, "🟠 Elevated Blood Pressure"),
            (135, 75, "🟡 Hypertension Stage 1"),  # Driven by systolic
            (118, 85, "🟡 Hypertension Stage 1"),  # Driven by diastolic
            (145, 82, "🔴 Hypertension Stage 2"),  # Driven by systolic
            (135, 95, "🔴 Hypertension Stage 2"),  # Driven by diastolic
            (185, 115, "🚨 Hypertensive Crisis"),   # Extreme systolic
            (170, 125, "🚨 Hypertensive Crisis"),   # Extreme diastolic
        ]
        for sys, dia, expected in test_cases:
            with self.subTest(sys=sys, dia=dia):
                self.assertEqual(classify_blood_pressure(sys, dia), expected)

    def test_invalid_types_raise_type_error(self):
        """Verifies that improper data structures throw explicit TypeErrors."""
        with self.assertRaises(TypeError):
            classify_blood_pressure("120", 80)
        with self.assertRaises(TypeError):
            classify_blood_pressure(120, [80])

    def test_out_of_bounds_values_raise_value_error(self):
        """Verifies that medically absurd parameters trigger targeted ValueErrors."""
        invalid_bounds = [
            (35, 80),   # Systolic too low
            (310, 80),  # Systolic too high
            (120, 15),  # Diastolic too low
            (120, 210)  # Diastolic too high
        ]
        for sys, dia in invalid_bounds:
            with self.subTest(sys=sys, dia=dia):
                with self.assertRaises(ValueError):
                    classify_blood_pressure(sys, dia)


# ==========================================
# 🖥️ INTERACTIVE USER INTERFACE CHANNEL
# ==========================================
def run_interactive_terminal():
    """
    Handles standalone interactive CLI terminal communication pipelines.
    """
    print("\n--- Interactive User Analysis Channel Initialized ---")
    try:
        sys_input = input("Enter Systolic pressure (top number): ")
        dia_input = input("Enter Diastolic pressure (bottom number): ")
        
        # Structural conversion checks
        sys = int(sys_input)
        dia = int(dia_input)
        
        analysis = classify_blood_pressure(sys, dia)
        print(f"\n📊 Diagnostic Output: {analysis}")
        
    except ValueError as val_err:
        print(f"\n❌ Execution Blocked (ValueError): {val_err}")
    except TypeError as type_err:
        print(f"\n❌ Execution Blocked (TypeError): {type_err}")
    finally:
        print("\n🧹 Diagnostics concluded. Terminal cache cleared.")


if __name__ == "__main__":
    print("--- Executing System Diagnostics ---")
    
    # 1. This invokes the unittest framework runner explicitly 
    # exit=False prevents execution from terminating before the interactive tool loads
    unittest.main(exit=False)
    
    # 2. Fire up user engine interface
    run_interactive_terminal()