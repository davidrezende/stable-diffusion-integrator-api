import replicate

def generate_stable_diffusion_img(prompt):
    print('inicio de execução')
    iterator = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": prompt}
    )
    for image in iterator:
        print('imagem gerada: ',image)
        print('fim de execução')
        return image

    