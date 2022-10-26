from sqlalchemy import Integer, String, Column, Table, MetaData, ForeignKey, select, create_engine, TIMESTAMP

meta = MetaData()

documents_model = Table('documents', meta,
                        Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('name', String),
                        Column('text', String),
                        Column('inserted_at', TIMESTAMP),
                        Column('updated_at', TIMESTAMP)
                        )

rights_model = Table('rights', meta,
                     Column('id', Integer, primary_key=True, autoincrement=True),
                     Column('document_id', Integer, ForeignKey('documents.id')),
                     Column('name', String),
                     Column('text', String),
                     Column('right_from', TIMESTAMP),
                     Column('rights_to', TIMESTAMP),
                     Column('inserted_at', TIMESTAMP),
                     Column('updated_at', TIMESTAMP)
                     )




