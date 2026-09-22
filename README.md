# Salary Predictor

A machine-learning salary prediction project with a Streamlit interface and a FastAPI prediction API. The project has been upgraded with FastAPI and Docker for a cleaner API workflow and easier deployment.

## Demo

[Open the Streamlit demo](https://salary-predictor-mat.streamlit.app/)

## Docker image

[View the Docker image on Docker Hub](https://hub.docker.com/r/tyhan55/salary-predictor-api)

## Project structure

```text
salary-predictor/
├── app/
│   ├── main.py             # FastAPI application and API routes
│   ├── model_service.py    # Loads the model and generates predictions
│   └── schema.py            # Request and response validation
├── Salary Data.csv         # Salary dataset
├── salary-predictor-model.ipynb  # Data preparation and model training
├── knn_model.joblib        # Trained KNN model
├── processor.joblib        # Saved preprocessing pipeline
├── streamlit_app.py        # Streamlit frontend
├── requirements.txt        # Python dependencies
└── dockerfile              # Docker configuration for the FastAPI API
```

## Install and run locally

### 1. Clone the repository

```bash
git clone https://github.com/tyhan-data/salary-predictor.git
cd salary-predictor
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

- Interactive API documentation: `http://127.0.0.1:8000/docs`
- Prediction endpoint: `POST /predict`

### 4. Run the Streamlit app

In a separate terminal, with the virtual environment activated:

```bash
streamlit run streamlit_app.py
```

## Run with Docker

Build the image from the project root:

```bash
docker build -f dockerfile -t salary-predictor-api .
```

Start the FastAPI container:

```bash
docker run -p 8000:8000 salary-predictor-api
```

The API documentation will be available at `http://localhost:8000/docs`.

### Run the published Docker image

```bash
docker pull tyhan55/salary-predictor-api
docker run -p 8000:8000 tyhan55/salary-predictor-api
```

## API request example

Send a `POST` request to `/predict` with:

```json
{
  "Age": 29,
  "Gender": "Male",
  "EducationLevel": "Bachelor's",
  "JobTitle": "Software Engineer",
  "YearsofExperience": 4
}
```

The API returns the predicted salary in the `Salary` field.
