from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import OptRequest, OptResponse
from app.optimizer import optimizar

app = FastAPI(
    title="Optimizador de Portafolio",
    version="1.0.0",
    description="Microservicio de optimización con restricción presupuestaria (0/1 knapsack).",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/optimizar", response_model=OptResponse)
def post_optimizar(req: OptRequest):
    """
    Endpoint para calcular la combinación óptima de proyectos que maximiza la ganancia sin superar la capacidad.
    """
    if req.capacidad < 0:
        raise HTTPException(status_code=400, detail="capacidad debe ser >= 0")
    if len(req.objetos) == 0:
        raise HTTPException(status_code=400, detail="lista de objetos vacía")
    if req.capacidad > 200_000:
        raise HTTPException(status_code=413, detail="capacidad demasiado grande para DP")

    ganancia_total, seleccionados, peso_total = optimizar(req.capacidad, req.objetos)
    return OptResponse(
        seleccionados=seleccionados,
        ganancia_total=ganancia_total,
        peso_total=peso_total
    )
