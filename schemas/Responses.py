from pydantic import BaseModel


class SuccessResponse(BaseModel):
    message: str
    status: int
    data: dict
    class Config:
        json_schema_extra  = {
            "example": {
                "message": "Success",
                "status": 200,
                "data": {}
            }
        }
        

class ErrorResponse(BaseModel):
    message: str
    status: int
    data: dict = {}
    class Config:
        json_schema_extra  = {
            "example": {
                "message": "Error",
                "status": 500,
                "data": {}
            }
        }