from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensagem": "Minha API está funcionando!"}


@app.get("/health")
def health():
    return {"status": "healthy"}