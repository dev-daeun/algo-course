# python3


class Query:
    def __init__(self, query):
        query = query.split()
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def test1():
    inputs = list()
    inputs.append(Query('add 911 police'))
    inputs.append(Query('add 76213 Mom'))
    inputs.append(Query('add 17239 Bob'))
    inputs.append(Query('find 76213'))
    inputs.append(Query('find 910'))
    inputs.append(Query('find 911'))
    inputs.append(Query('del 910'))
    inputs.append(Query('del 911'))
    inputs.append(Query('find 911'))
    inputs.append(Query('find 76213'))
    inputs.append(Query('add 76213 Dad'))
    inputs.append(Query('add 76213'))
    
    result = process_queries(inputs)

    assert result == [
        'Mom',
        'not found',
        'police',
        'not found',
        'Mom',
        'Dad',
    ]


def test2():
    inputs = list()
    inputs.append(Query('find 3839442'))
    inputs.append(Query('add 123456 me'))
    inputs.append(Query('add 0 granny'))
    inputs.append(Query('find 0'))
    inputs.append(Query('find 123456'))
    inputs.append(Query('del 0'))
    inputs.append(Query('del 0'))
    inputs.append(Query('find 0'))

    result = process_queries(inputs)

    assert result == [
        'not found',
        'granny',
        'me',
        'not found',
    ]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
