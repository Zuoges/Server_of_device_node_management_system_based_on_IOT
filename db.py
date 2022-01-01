import sqlite3

global dbconnect
dbconnect = sqlite3.connect('db/Server.db', check_same_thread=False)


def connect():
    print("open db successfully")


def insert(uuid, local, state, vlotage, current, apower, aelectricity,
           powerfactor, analysis, username, userid):
    cursor = dbconnect.cursor()
    sql = "insert into devicedata values(?,?,?,?,?,?,?,?,?,?,?)"
    data = (uuid, local, state, vlotage, current, apower, aelectricity,
            powerfactor, analysis, username, userid)
    cursor.execute(sql, data)
    cursor.close()
    dbconnect.commit()


def update(uuid, field, value):
    cursor = dbconnect.cursor()
    sql = "update devicedata set ?=? where uuid=?"
    data = (field, value, uuid)
    cursor.execute(sql, data)
    cursor.close()
    dbconnect.commit()


def update_all(uuid, local, state, vlotage, current, apower, aelectricity,
               powerfactor, analysis, username, userid):
    cursor = dbconnect.cursor()
    sql = "update devicedata set local=?, state=?, vlotage=?, current=?, apower=?, aelectricity=?, powerfactor=?, analysis=?, username=?, userid=? where uuid=?"
    data = (local, state, vlotage, current, apower, aelectricity, powerfactor,
            analysis, username, userid, uuid)
    cursor.execute(sql, data)
    cursor.close()
    dbconnect.commit()


def select_all():
    data = []
    bit = {}
    cursor = dbconnect.cursor()
    cursor.execute('select * from devicedata')
    for row in cursor:
        # print("uuid = " + str(row[0]))
        # print("local = " + str(row[1]))
        # print("state = " + str(row[2]))
        # print("vlotage = " + str(row[3]))
        # print("current = " + str(row[4]))
        # print("apower = " + str(row[5]))
        # print("aelectricity = " + str(row[6]))
        # print("powerfactor = " + str(row[7]))
        # print("analysis = " + str(row[8]))
        # print("username = " + str(row[9]))
        # print("userid = " + str(row[10]))
        # txt = str(row[0])+"\t"+str(row[1])+'\t'+str(row[2])+'\t'+str(row[3])+'\t'+str(row[4])+'\t'+str(row[5])+'\t'+str(row[6])+'\t'+str(row[7])+'\t'+str(row[8])+'\t'+str(row[9])+'\t'+str(row[10])
        bit['uuid'] = row[0]
        bit['local'] = row[1]
        bit['state'] = row[2]
        bit['vlotage'] = row[3]
        bit['current'] = row[4]
        bit['apower'] = row[5]
        bit['aelectricity'] = row[6]
        bit['powerfactor'] = row[7]
        bit['analysis'] = row[8]
        bit['username'] = row[9]
        bit['userid'] = row[10]
        data.append(bit)
        # print(data)
    cursor.close()
    dbconnect.commit()
    return data
