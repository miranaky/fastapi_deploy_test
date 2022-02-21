from fastapi import FastAPI
from fastapi.responses import JSONResponse

from graph import Graph
from models import Node, Edge, Job

app = FastAPI()


@app.post("/")
async def run(job: Job):
    nodes = job.dict().get("nodes")
    edges = job.dict().get("edges")
    result = topological_sort(nodes, edges)
    return JSONResponse({"result": result, "code": 200})


def topological_sort(nodes: list[Node], edges: list[Edge]):
    node_id_list = [node.get("id") for node in nodes]
    edge_list = [(edge.get("sourcePort").split(":")[0], edge.get("targetPort").split(":")[0]) for edge in edges]
    g = Graph(node_id_list)
    for edge in edge_list:
        g.addEdge(edge[0], edge[1])
    result = g.topologicalSort()
    return result
