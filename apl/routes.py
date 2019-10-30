from apl import apl

@apl.route('/')
@apl.route('/index')
def index():
    return "Halo, Dunia! di sini Flask"
