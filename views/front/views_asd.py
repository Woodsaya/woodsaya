from . import mod

@mod.get('/')
def index():
    return "HELLO"

@mod.get('/q')
def get_q():
    return "HELLO q"

@mod.get('/qwe')
def get_qwe():
    return "HELLO qwe"