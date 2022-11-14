import logging

from fastapi import APIRouter, BackgroundTasks

from src.operators.rights_table import *

rights_router = APIRouter()


@rights_router.post('/rights/create')
async def create_rights_table():
    create_rights_table.execute()
    return 'Таблица прав успешно создана'


@rights_router.post('/rights/add')
async def add_rights():
    insert_rights_table.execute()
    return 'Права успешно добавлены'


@rights_router.put('/rights/update')
async def update_rights():
    update_rights_table.execute()
    return 'Права успешно обновлены'


@rights_router.delete('/rights/delete')
async def delete_rights():
    drop_rights_table.execute()
    return 'Права успешно удалены'


@rights_router.get('/rights/<id>')
async def get_rights():
    # TODO create request
    pass


@rights_router.get('/rights')
async def get_all_rights():
    read_rights_table.execute()
    return 'Получены все права'
