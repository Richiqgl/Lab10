from database.DAO import  DAO
nazioni=DAO.getNazioni(2008)
print(len(nazioni))
confini=DAO.getConfini(2008)
print(confini)