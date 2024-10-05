from fastapi import FastAPI
from .database import engine
from .models import contact, deal, task
from .routers import contacts, deals, tasks

contact.Base.metadata.create_all(bind=engine)
deal.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contacts.router)
app.include_router(deals.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the CRM API"}