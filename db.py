import sqlite3 as db

conn = db.connect("./banco_dados.db")
cur = conn.cursor()

def new_table( table_name : str ):
    try:
        cur.execute(f"CREATE TABLE {table_name} ( nome , senha )")

        result = f"Comando ( {new_table.__name__} ) executado com sucesso!"
    except:

        result = "Erro na instrução SQL"

    return result

def get_tables():
    try:

        tables = []

        result = cur.execute("SELECT name FROM sqlite_master").fetchall()

        for i in result:
            
            table_name = i[0]
            tables.append(table_name)

            #table_info = cur.execute(f"SELECT * FROM {table_name}").description

            #fields = []
            #for x in table_info:
            #    fields.append( x[0] )
            #
            #columns = ",".join( fields )
            #print( f"{ table_name } : { columns }" )

    except:
        result = "Erro no SQL"
    
    return tables

def get_ususarios():

    SQL = "SELECT * FROM tbl_usuario"
    return cur.execute(SQL).fetchall()

def novousuario(nome:str,senha:str):
    if "tbl_usuario" not in get_tables():
        new_table("tbl_usuario")
    cur.execute(f"INSERT INTO tbl_usuario VALUES ('{nome}','{senha}')")
    conn.commit()
