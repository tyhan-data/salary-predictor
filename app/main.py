from fastapi import FastAPI
from contextlib import asynccontextmanager
from .model_service import load_artifacts, salary_predictor
from .schema import SalaryPredictorInput, SalaryPredictorOutput


# Using Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Starting the server...
    load_artifacts()
    # Closing the server.
    yield
    
    
app = FastAPI(
    title = "Salary Predictor",
    version = "2.2",
    lifespan= lifespan
)


@app.get("/")
def home_page():
    return {
        "message": "Welcome to our app",
        "status": "Success"
    }
    
    
@app.post("/predict", response_model=SalaryPredictorOutput)
def prediction(payload: SalaryPredictorInput):
    
    result = salary_predictor(payload.model_dump())
    
    return SalaryPredictorOutput(
        Salary= result["Salary"]
    )
    