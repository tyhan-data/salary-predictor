from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class GenderInfo(str, Enum):
    Male = "Male"
    Female = "Female"


class EducationLevelInfo(str, Enum):
    Bachelors = "Bachelor's"
    Masters = "Master's"
    PhD = "PhD"


class SalaryPredictorInput(BaseModel):

    Age: Annotated[
        int,
        Field(
            ...,
            ge=18,
            le=100,
            title="Age",
            description="Enter an age between 18 and 100",
            examples=[25],
        ),
    ]

    Gender: GenderInfo

    EducationLevel: EducationLevelInfo

    JobTitle: str=Field(..., min_length=2, max_length=50, examples=["Software Engineer"])     
    
    @field_validator("JobTitle")
    @classmethod
    def validate_job_title(cls, value: str):

        words = value.split()

        for word in words:
            if not word[0].isupper():
                raise ValueError(
                    "Each word must start with an uppercase letter."
                )

            if not word[1:].islower():
                raise ValueError(
                    "The remaining characters of each word must be lowercase."
                )

        return value
    
    YearsofExperience: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=60,
            title="Years of Experience",
            description="Enter years of experience between 0 and 50",
            examples=[5],
        ),
    ]


class SalaryPredictorOutput(BaseModel):
    Salary: float