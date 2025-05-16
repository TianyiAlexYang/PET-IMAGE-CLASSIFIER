from fastapi import FastAPI, UploadFile, File
from fastai.learner import load_learner
from fastai.vision.all import PILImage

app = FastAPI()
model = load_learner('model.pkl')

# Root route to confirm service is live
@app.get("/")
async def root():
    return {"message": "API is live. Use /predict to send POST requests with images."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = PILImage.create(await file.read())
    pred, _, probs = model.predict(img)
    return {"prediction": str(pred), "probabilities": probs.tolist()}
