from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from .templates import APOLLO_SANDBOX_HTML, GRAPHIQL_HTML, GRAPHQL_VOYAGER_HTML, PATHFINDER_IDE_HTML

try:
    import logging
    uvicorn_logger = logging.getLogger("uvicorn.error")
    uvicorn_logger.info(
        "GraphQL Explorer [FastAPI] enabled!"
        "\n\t Apollo Sandbox Explorer at:\t /  &  /explorer/apollo"
        "\n\t GraphiQL Playground at:\t /explorer/graphiql"
        "\n\t GraphQL Voyager at:\t\t /explorer/voyager"
        "\n\t GraphQL Voyager at:\t\t /explorer/pathfinder"
        "\n"
    )
except Exception:
    pass

router = APIRouter(tags=["GraphQL Router"])

@router.get("/explorer/apollo", name="Apollo Sandbox")
@router.get("/", name="Apollo Sandbox")
async def apollo_sandbox() -> HTMLResponse:
    return HTMLResponse(
        content=APOLLO_SANDBOX_HTML
    )


@router.get("/explorer/graphiql", name="GraphiQL Playground")
async def graphiql() -> HTMLResponse:
    return HTMLResponse(
        content=GRAPHIQL_HTML
    )

@router.get("/explorer/voyager", name="GraphQL Voyager")
async def voyager() -> HTMLResponse:
    return HTMLResponse(
        content=GRAPHQL_VOYAGER_HTML
    )

@router.get("/explorer/pathfinder", name="Pathfinder IDE")
async def voyager() -> HTMLResponse:
    return HTMLResponse(
        content=PATHFINDER_IDE_HTML
    )