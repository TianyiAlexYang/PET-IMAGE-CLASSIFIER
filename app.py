
from fastapi import FastAPI, UploadFile, File
from fastai.learner import load_learner
from fastai.vision.all import PILImage

app = FastAPI()
model = load_learner('model.pkl')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = PILImage.create(await file.read())
    pred, _, probs = model.predict(img)
    return {"prediction": str(pred), "probabilities": probs.tolist()}
