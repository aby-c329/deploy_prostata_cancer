from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib

app = FastAPI(
    title='deploy prostata cancer model',
    version='0.0.1'
)


@app.post('/api/v1/predict-prostata-cancer', tags=['prostata-cancer'])
async def predict(
    radius: float,
    texture: float,
    perimeter: float,
    area: float,
    smoothness: float,
    compactness: float,
    symmetry: float,
    fractal_dimension: float
):





    dictionary = {
        'radius': radius,
        'texture': texture,
        'perimeter': perimeter,
        'area': area,
        'smoothness': smoothness,
        'compactness': compactness,
        'symmetry': symmetry,
        'fractal_dimension': fractal_dimension
    }
    try:
        df_new_data = pd.DataFrame(data=dictionary, index=[0])
        #prediction = model.predict(df)
        return JSONResponse(
            statues_code=status.HTTP_200_OK,
            content='B'
        )
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )