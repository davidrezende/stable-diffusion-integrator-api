import generateimg

from fastapi import FastAPI

app = FastAPI()

@app.get("/generate/{prompt}")
def read_root(prompt):
    return {generateimg.generate_stable_diffusion_img(prompt)}

