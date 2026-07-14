from dataclasses import dataclass
from enum import Enum
import logging
import unittest

# Configure professional logging metrics
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

# ==========================================
# 🛑 CUSTOM DOMAIN EXCEPTIONS
# ==========================================
class BloodPressureError(ValueError):
    """Base domain exception for all blood pressure operations."""
    pass

class InvalidReadingError(BloodPressureError):
    """Raised when data fields are numeric but outside medically survival parameters."""
    pass


# ==========================================
# 🏷️ TYPE-SAFE CATEGORY ENUM
# ==========================================
class BPCategory(Enum):
    NORMAL = ("🟢 Normal Blood Pressure", "Ideal cardiovascular equilibrium.")
    ELEVATED = ("🟠 Elevated Blood Pressure", "Slightly elevated; lifestyle monitoring advised.")
    STAGE_1 = ("🟡 Hypertension Stage 1", "Persistent elevated boundary; clinical evaluation suggested.")
    STAGE_2 = ("🔴 Hypertension Stage 2", "High blood pressure status; medical intervention recommended.")
    CRISIS = ("🚨 Hypertensive Crisis", "Critical threshold passed! Seek emergency medical care immediately!")

    def __init__(self, label: str, description: str):
        self.label = label
        self.description = description


# ==========================================
# 📦 DATA ENCAPSULATION & LOGIC OBJECT
# ==========================================
@dataclass(frozen=True)
class BloodPressureReading:
    """
    Immutable data class capturing, validating, and self-analyzing
    individual patient blood pressure telemetry.
    """
    systolic: int | float
    diastolic: int | float

    def __post_init__(self):
        """Validates variables automatically upon object instantiation."""
        # 1. Type Enforcement
        if not isinstance(self.systolic, (int, float)) or not isinstance(self.diastolic, (int, float)):
            raise TypeError("Systolic and Diastolic inputs must be numerical integers or floats.")

        # 2. Medically Safe Boundary Validation
        if self.systolic <= 40 or self.systolic >= 300:
            raise InvalidReadingError(f"Absurd Systolic value ({self.systolic} mmHg). Bounds: 40-300.")
        if self.diastolic <= 20 or self.diastolic >= 200:
            raise InvalidReadingError(f"Absurd Diastolic value ({self.diastolic} mmHg). Bounds: 20-200.")

    def classify(self) -> BPCategory:
        """
        Executes hierarchical evaluation of the clinical parameters.
        """
        if self.systolic > 180 or self.diastolic > 120:
            return BPCategory.CRISIS
        elif self.systolic >= 140 or self.diastolic >= 90:
            return BPCategory.STAGE_2
        elif (130 <= self.systolic <= 139) or (80 <= self.diastolic <= 89):
            return BPCategory.STAGE_1
        elif (120 <= self.systolic <= 129) and self.diastolic < 80:
            return BPCategory.ELEVATED
        else:
            return BPCategory.NORMAL


# ==========================================
# 🧪 ROBUST AUTOMATED UNITTIEST SUITE
# ==========================================
class TestBloodPressurePipeline(unittest.TestCase):
    
    def test_valid_clinical_matrix(self):
        """Validates precision mappings across all standard medical zones."""
        matrix = [
            (115, 75, BPCategory.NORMAL),
            (125, 78, BPCategory.ELEVATED),
            (135, 75, BPCategory.STAGE_1),  # Systolic driven
            (118, 85, BPCategory.STAGE_1),  # Diastolic driven
            (145, 82, BPCategory.STAGE_2),  # Systolic driven
            (135, 95, BPCategory.STAGE_2),  # Diastolic driven
            (185, 115, BPCategory.CRISIS),  # Emergency systolic
            (170, 125, BPCategory.CRISIS),  # Emergency diastolic
        ]
        for sys, dia, expected_enum in matrix:
            with self.subTest(sys=sys, dia=dia):
                reading = BloodPressureReading(sys, dia)
                self.assertEqual(reading.classify(), expected_enum)

    def test_input_type_fault_handling(self):
        """Ensures structural type violations throw strict TypeErrors."""
        with self.assertRaises(TypeError):
            BloodPressureReading("120", 80)
        with self.assertRaises(TypeError):
            BloodPressureReading(120, None)

    def test_domain_boundary_rejection(self):
        """Ensures custom range exceptions correctly trap invalid data points."""
        bad_ranges = [(30, 80), (320, 80), (120, 10), (120, 220)]
        for sys, dia in bad_ranges:
            with self.subTest(sys=sys, dia=dia):
                with self.assertRaises(InvalidReadingError):
                    BloodPressureReading(sys, dia)


# ==========================================
# 🖥️ RUNTIME CONTROLLER INTERFACE
# ==========================================
def run_interactive_pipeline():
    """Manages application workflow execution and handles data entry."""
    print("\n" + "="*50)
    print("🏥 AUTOMATED CARDIO DIAGNOSTIC INTERFACE INITIALIZED")
    print("="*50)
    
    try:
        sys_raw = input("Enter Systolic Pressure (mmHg): ")
        dia_raw = input("Enter Diastolic Pressure (mmHg): ")
        
        # Parse inputs
        sys = float(sys_raw) if '.' in sys_raw else int(sys_raw)
        dia = float(dia_raw) if '.' in dia_raw else int(dia_raw)
        
        # Instantiate object (Auto-triggers validation checks)
        reading = BloodPressureReading(sys, dia)
        category = reading.classify()
        
        # Display success results via Logger
        logging.info(f"Successful Analysis Generated for {sys}/{dia} mmHg")
        print(f"\n📊 DIAGNOSTIC RESULTS:")
        print(f"   Category:    {category.label}")
        print(f"   Description: {category.description}")
        
    except ValueError as ex:
        # Catches bad text strings OR custom InvalidReadingErrors
        logging.error(f"Data entry processing aborted: {ex}")
    except TypeError as ex:
        logging.error(f"Type constraint mapping failed: {ex}")
    finally:
        print("="*50)
        print("🧹 Core engine cache purged. Diagnostic channel offline.")
        print("="*50 + "\n")


if __name__ == "__main__":
    logging.info("Initiating structural system diagnostics check...")
    
    # Run the tests quietly, then kick off the terminal loop
    runner = unittest.TextTestRunner(verbosity=1)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBloodPressurePipeline)
    test_result = runner.run(suite)
    
    if test_result.wasSuccessful():
        logging.info("All 14 unit test arrays successfully validated. Loading CLI runtime context...")
        run_interactive_pipeline()
    else:
        logging.critical("System tests failed! Blocking interface authorization initialization workflow.")