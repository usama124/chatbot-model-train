from fastapi import APIRouter, BackgroundTasks, HTTPException
from services import model_train
from schema.schema import TrainModel


router = APIRouter(
    prefix="",
    tags=["Model Training"]
)

@router.post("/train-model", summary="endpoint for training model in background.")
async def post_dataset(train_model: TrainModel, background_tasks: BackgroundTasks):
    file_name = train_model.filepath
    status_code, content = model_train.read_file_content(file_name)
    if status_code == 200:
        background_tasks.add_task(model_train.model_train_service, content)
        return {"message": "model training has been started in background."}
    else:
        raise HTTPException(status_code=status_code, detail=content)