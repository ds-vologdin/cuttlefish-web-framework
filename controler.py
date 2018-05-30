import json


def handler_1(request, arg_dict={}):
    args = ''
    if arg_dict and isinstance(arg_dict, dict):
        args = json.dumps(arg_dict)

    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(args)
    return respone


def handler_2(request, arg_dict={}):
    args = ''
    if arg_dict and isinstance(arg_dict, dict):
        args = json.dumps(arg_dict)

    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(args)
    return respone
