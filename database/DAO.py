from database.DB_connect import DBConnect
from modello.nazioni import Nazione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNazioni(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT c.*
                FROM country c 
                WHERE c.CCode in (SELECT state1no AS stato 
                FROM contiguity WHERE `year` <= %s 
                UNION
                SELECT state2no AS stato
                FROM contiguity
                WHERE `year` <= %s  )
                ORDER BY c.StateNme ASC"""
        cursor.execute(query, (anno,anno))

        for row in cursor:
            result.append(Nazione(**row))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getConfini(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT state1no ,state2no 
                FROM contiguity
                WHERE `year` < %s AND conttype = 1"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result


