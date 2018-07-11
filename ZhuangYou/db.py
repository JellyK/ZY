import pymysql

USER = 'user'
PASSWORD = 'passw0rd'
DB = 'zhuangyou'

class DB():
    def __init__(self, user=USER, password=PASSWORD, db=DB):
        self.user = user
        self.password = password
        self.db = self.initDB(user, password, db)

    def initDB(self, user, password, db):
        return pymysql.connect('localhost', user, password, db)

    def checkTables(self):
        cursor = self.db.cursor()
        cursor.execute('show tables')
        data = cursor.fetchall()
        print(data)

    def initTables(self):
        self.createTable('echarge')

    def createTable(self, table):
        cursor = self.db.cursor()
        create_table = '''create table if not exists {}(
            _id int auto_increment primary key,
            address varchar(128) NOT NULL,
            areaName varchar(128),
            city varchar(16),
            company varchar(128),
            connectorType int,
            currentType int,
            freeNum int,
            id varchar(64),
            images blob,
            isGs int,
            lat float,
            link int,
            lng float,
            mapIcon varchar(128),
            maxOutPower int,
            operatorTypes varchar(1),
            payType varchar(16),
            phone varchar(16),
            plugType int,
            priceRational int,
            province varchar(16),
            quantity int,
            score int,
            serviceCode int,
            standard int,
            status int,
            supportOrder int)
            engine=InnoDB default charset=utf8;
        '''.format(table)
        cursor.execute(create_table)

    def deleteTable(self, table):
        cursor = self.db.cursor()
        drop_table = 'drop table if exists {}'.format(table)
        cursor.execute(drop_table)

    def closeDB(self):
        self.db.close()

if __name__ == '__main__':
    db = DB()
    db.createTable('echarge')
    # db.deleteTable('echarge')
    db.checkTables()
