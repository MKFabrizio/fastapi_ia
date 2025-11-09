from fastapi import FastAPI, HTTPException
from models import load_text_model, generate_text

app = FastAPI()