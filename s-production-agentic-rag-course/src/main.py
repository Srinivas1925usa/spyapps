# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import get_settings
from src.db.factory import make_database
from src.routers import ping, ask, papers


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    )
logger = logging.getLogger(__name__)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@asynccontextmanager
async def lifespan(app: FastAPI):
    """ Week1: simplified lifespan for learning purposes
    """

    logger.info('Starting RAG API...')

    settings = get_settings()
    app.state.settings = settings

    database = make_database()
    app.state.database = database
    logger.info("Database connected")

    # Placeholders for future weeks
    app.state.pdf_parser_service = None
    app.state.opensearch_service = None
    app.state.llm_service = None

    logger.info('RAG API is READY...')
    yield
app = FastAPI(
    title="arXiv Paper Curator API",
    root_path="/api/v1",
    description="Personal arXiv CS.AI paper curator with RAG capabilities",
    version=os.getenv("APP_VERSION", "0.1.0"),
)
app.include_router(ping.router)
app.include_router(ask.router)
app.include_router(papers.router)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import uvicorn
    uvicorn.run('main:app', port=8000, host="0.0.0.0", reload=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
