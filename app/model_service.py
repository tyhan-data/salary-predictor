from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "knn_model.joblib"
PROCESSOR_PATH = BASE_DIR / "processor.joblib"

_model = None
_processor = None


def load_artifacts():
    global _model, _processor

    if _model is None:
        _model = joblib.load(MODEL_PATH)

    if _processor is None:
        _processor = joblib.load(PROCESSOR_PATH)


def salary_predictor(data: dict):
    load_artifacts()

    # Convert input dictionary to DataFrame
    X = pd.DataFrame([{
        "Age": data["Age"],
        "Gender": data["Gender"],
        "Education Level": data["EducationLevel"],
        "Job Title": data["JobTitle"],
        "Years of Experience": data["YearsofExperience"],
    }])

    # Preprocess
    X = _processor.transform(X)

    # Prediction
    prediction = _model.predict(X)[0]

    return {
        "Salary": float(prediction)
    }