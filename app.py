from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastai.learner import load_learner
from fastai.vision.all import PILImage
from io import BytesIO
from PIL import Image  # Explicitly import PIL's Image

app = FastAPI()
model = load_learner('model.pkl')

@app.get("/")
async def root():
    return {"message": "API is live. Use /predict to send POST requests with images."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        img_bytes = await file.read()
        pil_img = Image.open(BytesIO(img_bytes)).convert("RGB")  # Ensure RGB format
        img = PILImage.create(pil_img)
        pred, _, probs = model.predict(img)
        return {"prediction": str(pred), "probabilities": probs.tolist()}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
