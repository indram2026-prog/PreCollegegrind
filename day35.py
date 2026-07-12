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


def run_automated_tests():
    """
    Programmatically executes test suites covering standard outcomes,
    boundary values, and targeted exception throwing.
    """
    print("🧪 Starting Automated Test Suite...\n")
    
    # Format: (systolic, diastolic, expected_outcome_or_exception)
    valid_test_cases = [
        (115, 75, "🟢 Normal Blood Pressure"),
        (125, 78, "🟠 Elevated Blood Pressure"),
        (135, 75, "🟡 Hypertension Stage 1"),  # Driven by systolic boundary
        (118, 85, "🟡 Hypertension Stage 1"),  # Driven by diastolic boundary
        (145, 82, "🔴 Hypertension Stage 2"),  # Driven by systolic
        (135, 95, "🔴 Hypertension Stage 2"),  # Driven by diastolic
        (185, 115, "🚨 Hypertensive Crisis"),  # Extreme systolic
        (170, 125, "🚨 Hypertensive Crisis"),  # Extreme diastolic
    ]
    
    exception_test_cases = [
        ("120", 80, TypeError),    # String input type failure
        (120, [80], TypeError),    # List input type failure
        (35, 80, ValueError),      # Too low systolic boundary
        (310, 80, ValueError),     # Too high systolic boundary
        (120, 15, ValueError),      # Too low diastolic boundary
        (120, 210, ValueError),     # Too high diastolic boundary
    ]

    passed_tests = 0
    total_tests = len(valid_test_cases) + len(exception_test_cases)

    # Suite 1: Verify Valid Structural Calculations
    for sys, dia, expected in valid_test_cases:
        try:
            result = classify_blood_pressure(sys, dia)
            assert result == expected, f"Expected '{expected}', got '{result}'"
            print(f"✅ Pass: {sys}/{dia} mmHg properly categorized as -> {result}")
            passed_tests += 1
        except AssertionError as err:
            print(f"❌ Fail: Test {sys}/{dia} failed assertion! Details: {err}")

    # Suite 2: Verify Exception Raising Safety Nets
    for sys, dia, expected_exception in exception_test_cases:
        try:
            classify_blood_pressure(sys, dia)
            print(f"❌ Fail: Input ({sys}, {dia}) failed to raise expected {expected_exception.__name__}")
        except (TypeError, ValueError) as caught_err:
            if isinstance(caught_err, expected_exception):
                print(f"✅ Pass: {sys}/{dia} successfully triggered error tracking -> [{type(caught_err).__name__}]: {caught_err}")
                passed_tests += 1
            else:
                print(f"❌ Fail: Expected {expected_exception.__name__}, but caught {type(caught_err).__name__} instead.")

    print(f"\n📊 Test Suite Summary: Passed {passed_tests}/{total_tests} test scenarios.\n")


def run_interactive_terminal():
    """
    Handles standard manual CLI interactive sessions with standalone error catch states.
    """
    print("--- Interactive User Analysis Channel Initialized ---")
    try:
        sys_input = input("Enter Systolic pressure (top number): ")
        dia_input = input("Enter Diastolic pressure (bottom number): ")
        
        # Safe structural parsing check
        sys = int(sys_input)
        dia = int(dia_input)
        
        analysis = classify_blood_pressure(sys, dia)
        print(f"\n📊 Diagnostic Output: {analysis}")
        
    except ValueError as val_err:
        print(f"\n❌ Execution Blocked (ValueError): {val_err}")
    except TypeError as type_err:
        print(f"\n❌ Execution Blocked (TypeError): {type_err}")
    finally:
        print("\n🧹 Diagnostics concluded. System clearing terminal cache state.")


if __name__ == "__main__":
    # 1. Run the entire automated validation suite
    run_automated_tests()
    
    # 2. Boot up the interactive utility interface
    run_interactive_terminal()