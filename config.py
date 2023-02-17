import os
DB_URI = "mongodb+srv://sagar:<sagar123@cluster0.rd1gxhm.mongodb.net/?retryWrites=true&w=majority"
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x16\xbfI\xc9\x0f\xd2\xb1\x1f\xf2n\xb8`\x1frdw'
    
    MONGODB_SETTINGS = {'host': os.environ.get('MONGODB_URI', DB_URI)} 


