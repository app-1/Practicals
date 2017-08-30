user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
              'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
              'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_prompt = input('Username: ')

if user_prompt in user_names:
    print('Access granted')
else:
    print('Access denied')