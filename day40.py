from dataclasses import dataclass
from enum import Enum
import logging
import sys
import unittest
from typing import Callable

# Configure isolated, professional logging metrics to prevent stream pollution
logger = logging.getLogger("CardioDiagnostic")
logger.setLevel(logging.INFO)

# Avoid adding duplicate handlers if this script is imported elsewhere
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# ==========================================
# 🛑 CUSTOM DOMAIN EXCEPTIONS
# ==========================================
class BloodPressureError(ValueError):
    """Base domain exception for all blood pressure operations."""
    pass


class InvalidReadingError(BloodPressureError):
    """Raised when data fields are numeric but outside medically survivable parameters."""
    def __init__(self, message: str, value: int | float):
        super().__init__(message)
        self.invalid_value = value


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

    def __post_init__(self) -> None:
        """Validates variables automatically upon object instantiation.
        
        Raises:
            TypeError: If input values are not numbers (e.g., strings or booleans).
            InvalidReadingError: If values fall outside medically survivable limits.
        """
        # 1. Type Enforcement (Explicitly weed out booleans, which are subclasses of int)
        if not isinstance(self.systolic, (int, float)) or isinstance(self.systolic, bool):
            raise TypeError("Systolic input must be a numerical integer or float.")
        if not isinstance(self.diastolic, (int, float)) or isinstance(self.diastolic, bool):
            raise TypeError("Diastolic input must be a numerical integer or float.")

        # 2. Medically Safe Boundary Validation
        if not (40 <= self.systolic <= 300):
            raise InvalidReadingError(f"Absurd Systolic value ({self.systolic} mmHg). Bounds: 40-300.", self.systolic)
        if not (20 <= self.diastolic <= 200):
            raise InvalidReadingError(f"Absurd Diastolic value ({self.diastolic} mmHg). Bounds: 20-200.", self.diastolic)

    def classify(self) -> BPCategory:
        """Executes clinical assessment of the parameters using a hierarchical mapping.
        
        Returns:
            BPCategory: The evaluated severity category.
        """
        if self.systolic > 180 or self.diastolic > 120:
            return BPCategory.CRISIS
        if self.systolic >= 140 or self.diastolic >= 90:
            return BPCategory.STAGE_2
        if (130 <= self.systolic <= 139) or (80 <= self.diastolic <= 89):
            return BPCategory.STAGE_1
        if (120 <= self.systolic <= 129) and self.diastolic < 80:
            return BPCategory.ELEVATED
        return BPCategory.NORMAL


# ==========================================
# 🧪 ROBUST AUTOMATED UNIT TEST SUITE
# ==========================================
class TestBloodPressurePipeline(unittest.TestCase):
    
    def test_valid_clinical_matrix(self) -> None:
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
        for sys_val, dia_val, expected_enum in matrix:
            with self.subTest(sys=sys_val, dia=dia_val):
                reading = BloodPressureReading(sys_val, dia_val)
                self.assertEqual(reading.classify(), expected_enum)

    def test_input_type_fault_handling(self) -> None:
        """Ensures structural type violations throw strict TypeErrors."""
        with self.assertRaises(TypeError):
            BloodPressureReading("120", 80) # type: ignore
        with self.assertRaises(TypeError):
            BloodPressureReading(120, None) # type: ignore
        with self.assertRaises(TypeError):
            BloodPressureReading(True, 80) # Booleans inherit from int, catch explicitly

    def test_domain_boundary_rejection(self) -> None:
        """Ensures custom range exceptions correctly trap invalid data points."""
        bad_ranges = [(39.9, 80), (300.1, 80), (120, 19.9), (120, 200.1)]
        for sys_val, dia_val in bad_ranges:
            with self.subTest(sys=sys_val, dia=dia_val):
                with self.assertRaises(InvalidReadingError) as context:
                    BloodPressureReading(sys_val, dia_val)
                # Verify telemetry capture inside the custom exception payload
                self.assertIn(context.exception.invalid_value, [sys_val, dia_val])


# ==========================================
# 🖥️ RUNTIME CONTROLLER INTERFACE
# ==========================================
def parse_numeric_input(prompt: str, input_func: Callable[[str], str] = input) -> int | float | None:
    """Helper to safely request and parse numeric console input with recovery retries.
    
    Allows user to type 'q' or 'exit' to cleanly abort.
    """
    while True:
        try:
            raw = input_func(prompt).strip().lower()
            if raw in ('q', 'exit', 'quit'):
                return None
            if not raw:
                raise ValueError("Input field cannot be left blank.")
            
            # Check if floating point calculation is necessary
            if '.' in raw:
                return float(raw)
            return int(raw)
        except ValueError as ex:
            print(f"⚠️  Invalid raw input: {ex}. Please enter a valid number, or 'q' to quit.")


def run_interactive_pipeline(input_func: Callable[[str], str] = input) -> None:
    """Manages CLI execution loop, user prompts, and parsing pipelines."""
    print("\n" + "="*50)
    print("🏥 AUTOMATED CARDIO DIAGNOSTIC INTERFACE INITIALIZED")
    print("   (Type 'q' or 'quit' at any prompt to exit cleanly)")
    print("="*50)
    
    try:
        # Prompting users with native recovery loop
        sys_val = parse_numeric_input("Enter Systolic Pressure (mmHg): ", input_func)
        if sys_val is None:
            logger.info("Session terminated by user request.")
            return
            
        dia_val = parse_numeric_input("Enter Diastolic Pressure (mmHg): ", input_func)
        if dia_val is None:
            logger.info("Session terminated by user request.")
            return
        
        # Instantiate immutable data model (Self-validates instantly)
        reading = BloodPressureReading(sys_val, dia_val)
        category = reading.classify()
        
        # Success reporting
        logger.info(f"Successful Analysis Generated for {sys_val}/{dia_val} mmHg")
        print(f"\n📊 DIAGNOSTIC RESULTS:")
        print(f"   Category:    {category.label}")
        print(f"   Description: {category.description}")
        
    except (InvalidReadingError, TypeError) as ex:
        logger.error(f"Diagnostic calculation aborted: {ex}")
    finally:
        print("="*50)
        print("🧹 Core engine cache purged. Diagnostic channel offline.")
        print("="*50 + "\n")


if __name__ == "__main__":
    logger.info("Initiating structural system diagnostics check...")
    
    # Temporarily silence warnings/logs during unit tests to keep terminal stdout pristine
    logger.setLevel(logging.WARNING)
    
    runner = unittest.TextTestRunner(verbosity=1)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBloodPressurePipeline)
    test_result = runner.run(suite)
    
    # Restore log levels to standard reporting
    logger.setLevel(logging.INFO)
    
    if test_result.wasSuccessful():
        logger.info("All unit test assertions successfully validated. Loading CLI runtime context...")
        run_interactive_pipeline()
    else:
        logger.critical("System tests failed! Blocking interface initialization workflow.")
        sys.exit(1)