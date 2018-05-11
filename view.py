def handler_1(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish<p>
        <p>argument 1: {0}<p>
    </body>
</html>
    '''.format(arg_dict.get('arg_key1', 'arg_key1 is not set'))
    return respone


def handler_2(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish<p>
        <p>argument 2: {0}<p>
    </body>
</html>
    '''.format(arg_dict.get('arg_key2', 'arg_key2 is not set'))
    return respone
