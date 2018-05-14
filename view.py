import json


def handler_1(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(json.dump(arg_dict))
    return respone


def handler_2(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(json.dumps(arg_dict))
    return respone
