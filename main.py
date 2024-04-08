from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib

app = FastAPI(
    title="Apis task 6",
    version="0.0.1"
)

#-------------------------------------------------------------
# LOAD MODEL
#-------------------------------------------------------------

model = joblib.load("model/logistic_regression_model_v01.pkl")


@app.post("/api/v1/apple-sorter", tags=["apple-sorter"])
async def predict(
    Size: float,
    Weight: float,
    Sweetness: float,
    Crunchiness: float,
    Juiciness: float,
    Ripeness: float,
    Acidity: float
):

    dictionary = {
        'Size': Size,
        'Weight': Weight,
        'Sweetness': Sweetness,
        'Crunchiness': Crunchiness,
        'Juiciness': Juiciness,
        'Ripeness': Ripeness,
        'Acidity': Acidity
    }

    try:
        df = pd.DataFrame(dictionary, index=[0])
        prediction = model.predict(df)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content= 1
        )
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_400_BAD_REQUEST

        )
