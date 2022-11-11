import logging

from fastapi import APIRouter, BackgroundTasks

from src.operators.documents_table import (create_db_documents,
                                           drop_db_documents,
                                           insert_db_documents,
                                           read_db_documents,
                                           update_db_documents)

documents_router = APIRouter()


@documents_router.post('/create/documents')
async def create_documents_table():
    create_db_documents.CreateDocumentTable.execute()
    return 'База данных документов успешно создана'


@documents_router.post('/document/add')
async def add_document():
    insert_db_documents.InsertDocumentTable.execute()
    return 'Документ усмешно добавлен'


@documents_router.put('/document/update')
async def update_document():
    update_db_documents.UpdateDocumentsTable.execute()
    return 'Документ успешно обновлён'


@documents_router.delete('/document/delete')
async def delete_document():
    drop_db_documents.DropDocumentsTable.execute()
    return 'Документ успешно удалён'


@documents_router.get('/document/<id>')
async def get_document():
    # TODO create request
    pass


@documents_router.get('/document')
async def get_all_documents():
    read_db_documents.ReadDocumentTable.execute()
    return 'Документы предоставлены для чтения'
