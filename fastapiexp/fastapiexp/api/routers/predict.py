from typing import Dict, List

from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/classification", tags=["classification"])
async def predict_classification(
    file: UploadFile = File(None, description="uploaded file by user"),
) -> List[Dict[str, float]]:
    contents = await file.read()
    print(contents)
    return [{}]
