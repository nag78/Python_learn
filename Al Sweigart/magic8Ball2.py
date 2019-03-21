from random import randint


messages = ['It is certain', 'It is decidedly so', 'Yes definitely',
            'Reply hazy try again', 'Ask again later', 'Concentrate and ask again',
            'My reply is no', 'Outlook not so good', 'Very doubful']


print(messages[randint(0, len(messages) - 1)])
