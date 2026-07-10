def classify_blood_pressure(systolic: int, diastolic: int) -> str:
    """
    Classifies blood pressure based on hardcoded medical thresholds.
    Takes systolic and diastolic values as integers.
    """
    # 1. Crisis Check (Highest Priority)
    if systolic > 180 or diastolic > 120:
        return "🚨 Hypertensive Crisis (Seek Emergency Medical Care Immediately!)"
    
    # 2. Stage 2 Hypertension Check
    elif systolic >= 140 or diastolic >= 90:
        return "🔴 High Blood Pressure (Hypertension Stage 2)"
    
    # 3. Stage 1 Hypertension Check
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "🟡 High Blood Pressure (Hypertension Stage 1)"
    
    # 4. Elevated Check
    elif (120 <= systolic <= 129) and diastolic < 80:
        return "🟠 Elevated Blood Pressure"
    
    # 5. Normal Check
    elif systolic < 120 and diastolic < 80:
        return "🟢 Normal Blood Pressure"
    
    # Catch-all fallback for boundary gaps
    else:
        return "⚠️ Mixed Reading (Consult a Doctor for Evaluation)"


# --- Test Cases ---
if __name__ == "__main__":
    print("--- Blood Pressure Classification Engine ---\n")
    
    # Test 1: Optimal Normal Reading
    sys1, dia1 = 115, 75
    print(f"Reading: {sys1}/{dia1} mmHg -> {classify_blood_pressure(sys1, dia1)}")
    
    # Test 2: Elevated Reading
    sys2, dia2 = 125, 78
    print(f"Reading: {sys2}/{dia2} mmHg -> {classify_blood_pressure(sys2, dia2)}")
    
    # Test 3: Stage 1 Hypertension (driven by diastolic)
    sys3, dia3 = 118, 85
    print(f"Reading: {sys3}/{dia3} mmHg -> {classify_blood_pressure(sys3, dia3)}")
    
    # Test 4: Stage 2 Hypertension (driven by systolic)
    sys4, dia4 = 145, 82
    print(f"Reading: {sys4}/{dia4} mmHg -> {classify_blood_pressure(sys4, dia4)}")
    
    # Test 5: Critical Warning Reading
    sys5, dia5 = 185, 125
    print(f"Reading: {sys5}/{dia5} mmHg -> {classify_blood_pressure(sys5, dia5)}")