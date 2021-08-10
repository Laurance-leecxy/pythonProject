from utils import get_mysql_msg

params = get_mysql_msg('prod')
DB_USER = params['DB_USER']
DB_PASS = params['DB_PASS']
DB_HOST = params['DB_HOST']
DB_PORT = params['DB_PORT']
DATABASE = params['DATABASE']

config = {
            'host': DB_HOST,
            'user': DB_USER,
            'password': DB_PASS,
            'database': DATABASE,
            'charset': 'utf8mb4',
            'port': DB_PORT
        }

connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT,DATABASE)