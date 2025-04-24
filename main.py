from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.db import create_tables, delete_tables
from api.users import router as users_router
from api.tasks import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена...")
    await create_tables()
    print("... и готова к работе")
    yield
    print("stopping...")


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(tasks_router)
