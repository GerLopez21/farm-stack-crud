from fastapi import APIRouter,HTTPException
from database import get_all_tasks,create_task,get_one_task,get_one_task_id,delete_task,update_task
from models import Task, UpdateTask
task =  APIRouter()
@task.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks

@task.post('/api/tasks',response_model=Task)
async def save_task(task:Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(409,"Task already exists")
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400,'Task hasnt been saved')
    
@task.get('/api/tasks/{id}',response_model=Task)
async def get_task(id:str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404,f"Task with id {id} not found")

@task.put('/api/tasks/{id}')
async def put_tasks(id:str,task:UpdateTask):
    response = await update_task(id,task)
    if response:
        return "Succesfuly updated"
    raise HTTPException(404,f"Task with id {id} not found")    

@task.delete('/api/tasks/{id}')
async def remove_tasks(id: str):
    response = await delete_task(id)
    if response:
        return "Succesfuly deleted"
    raise HTTPException(404,f"Task with id {id} not found")