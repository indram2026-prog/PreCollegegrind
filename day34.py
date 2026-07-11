def classify_blood_pressure(systolic: int, diastolic: int) -> str:
    """
    Classifies blood pressure based on hardcoded medical thresholds.
    Includes comprehensive input validation.
    """
    # 1. Type Validation (Check if inputs are actual numbers)
    if not isinstance(systolic, (int, float)) or not isinstance(diastolic, (int, float)):
        raise TypeError("Inputs must be numeric integers or floats.")

    # 2. Value Validation (Check for medically impossible ranges)
    if systolic <= 40 or systolic >= 300:
        raise ValueError(f"Invalid Systolic value ({systolic}). Must be between 40 and 300 mmHg.")
    if diastolic <= 20 or diastolic >= 200:
        raise ValueError(f"Invalid Diastolic value ({diastolic}). Must be between 20 and 200 mmHg.")

    # --- Core Classification Logic ---
    # Crisis Check (Highest Priority)
    if systolic > 180 or diastolic > 120:
        return "🚨 Hypertensive Crisis (Seek Emergency Medical Care Immediately!)"
    
    # Stage 2 Hypertension Check
    elif systolic >= 140 or diastolic >= 90:
        return "🔴 High Blood Pressure (Hypertension Stage 2)"
    
    # Stage 1 Hypertension Check
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "🟡 High Blood Pressure (Hypertension Stage 1)"
    
    # Elevated Check
    elif (120 <= systolic <= 129) and diastolic < 80:
        return "🟠 Elevated Blood Pressure"
    
    # Normal Check
    elif systolic < 120 and diastolic < 80:
        return "🟢 Normal Blood Pressure"
    
    else:
        return "⚠️ Mixed Reading (Consult a Doctor for Evaluation)"


def run_classification_system():
    """
    Wrapper function demonstrating try / except / finally error handling rules.
    """
    print("--- Secure Blood Pressure Analysis Booting ---")
    
    try:
        # Prompt user inputs
        sys_input = input("Enter Systolic pressure (top number): ")
        dia_input = input("Enter Diastolic pressure (bottom number): ")
        
        # This conversion step can trigger a ValueError if text is typed
        sys = int(sys_input)
        dia = int(dia_input)
        
        # This function call can trigger custom TypeErrors or ValueErrors
        result = classify_blood_pressure(sys, dia)
        print(f"\n📊 Result Analysis: {result}")
        
    except ValueError as val_err:
        # Catches bad text strings OR out-of-bounds medical values
        print(f"\n❌ Input Value Error: {val_err}")
        print("Please verify the numbers entered are realistic.")
        
    except TypeError as type_err:
        # Catches direct type mismatches
        print(f"\n❌ Data Type Error: {type_err}")
        
    except Exception as general_err:
        # Catch-all backup safety net
        print(f"\n⚡ An unexpected critical failure occurred: {general_err}")
        
    finally:
        # This clean-up line executes absolutely every single time
        print("\n🧹 Memory Status: Analysis run concluded. Diagnostic channel closed.")


# --- Execution ---
if __name__ == "__main__":
    run_classification_system()