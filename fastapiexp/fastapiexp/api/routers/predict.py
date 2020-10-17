from typing import Dict, List, Optional

from fastapi import APIRouter, Cookie, File, UploadFile

router = APIRouter()


@router.post("/classification", tags=["classification"])
async def predict_classification(
    file: UploadFile = File(None, description="uploaded file by user"),
    session_id: Optional[str] = Cookie(None),
) -> List[Dict[str, float]]:
    contents = await file.read()
    print(contents)
    return [{}]
