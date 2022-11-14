from src.operators.documents_table.update_db_documents import UpdateDocumentsTable
from src.operators.rights_table.create_db_rights import CreateRightsTable
from src.operators.rights_table.drop_db_rights import DropRightsTable
from src.operators.rights_table.insert_db_rights import InsertRightModel
from src.operators.rights_table.read_db_rights import ReadRightsTable

create_rights_table = CreateRightsTable()
drop_rights_table = DropRightsTable()
insert_rights_table = InsertRightModel()
read_rights_table = ReadRightsTable()
update_rights_table = UpdateDocumentsTable()
