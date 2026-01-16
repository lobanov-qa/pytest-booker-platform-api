from pydantic import BaseModel, Field, ConfigDict


class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    error_code: int = Field(alias="errorCode")
    error: str
    error_message: str = Field(alias="errorMessage")
    field_errors: list[str] = Field(alias="fieldErrors")


class BaseErrorResponse(BaseModel):
    """
    Standard Spring Boot error.
    """
    timestamp: str
    status: int
    error: str
    path: str
