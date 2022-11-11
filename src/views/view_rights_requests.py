import logging

from fastapi import APIRouter, BackgroundTasks

from src.operators.rights_table import (create_db_rights,
                                        drop_db_rights,
                                        insert_db_rights,
                                        read_db_rights,
                                        update_db_rights)

rights_router = APIRouter()


@rights_router.post('/create/rights')
async def create_rights_table():
    create_db_rights.CreateRightsTable.execute()
    return 'Таблица прав успешно создана'


@rights_router.post('/rights/add')
async def add_rights():
    insert_db_rights.InsertRightModel.execute()
    return 'Права успешно добавлены'


@rights_router.put('/rights/update')
async def update_rights():
    update_db_rights.UpdateDocumentsTable.execute()
    return 'Права успешно обновлены'


@rights_router.delete('/rights/delete')
async def delete_rights():
    drop_db_rights.DropRightsTable.execute()
    return 'Права успешно удалены'


@rights_router.get('/rights/<id>')
async def get_rights():
    # TODO create request
    pass


@rights_router.get('/rights')
async def get_all_rights():
    read_db_rights.ReadRightsTable.execute()
    return 'Получены все права'
