import pickle

FILE_NAME = 'domain/app_info.pickle'

def save(app):
    with open(FILE_NAME,'wb') as f:
        pickle.dump(app,f)
        
def load():
    try:
        with open(FILE_NAME,'rb') as f:
            return pickle.load(f)
    except Exception as e:
        return None