from src.operators.documents_table.create_db_documents import CreateDocumentTable
from src.operators.documents_table.drop_db_documents import DropDocumentsTable
from src.operators.documents_table.insert_db_documents import InsertDocumentTable
from src.operators.documents_table.read_db_documents import ReadDocumentTable
from src.operators.documents_table.update_db_documents import UpdateDocumentsTable

create_doc_table = CreateDocumentTable()
drop_doc_table = DropDocumentsTable()
ins_doc_table = InsertDocumentTable()
read_doc_table = ReadDocumentTable()
update_doc_table = UpdateDocumentsTable()
