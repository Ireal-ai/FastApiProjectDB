from fastapi import APIRouter
from src.operators.documents_table import *

documents_router = APIRouter()


@documents_router.get('/')
async def root():
    return 'Сервис для документов и прав'


@documents_router.post('/documents/create')
async def create_documents_table():
    create_doc_table.execute()
    return 'База данных документов успешно создана'


@documents_router.post('/document/add')
async def add_document():
    ins_doc_table.execute()
    return 'Документ усмешно добавлен'


@documents_router.put('/document/update')
async def update_document():
    update_doc_table.execute()
    return 'Документ успешно обновлён'


@documents_router.get('/document/delete')
async def delete_document():
    drop_doc_table.execute()
    return 'Документ успешно удалён'


@documents_router.get('/document/<id>')
async def get_document():
    # TODO create request
    pass


@documents_router.get('/document')
async def get_all_documents():
    read_doc_table.execute()
    return 'Документы предоставлены для чтения'
