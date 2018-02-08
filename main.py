from aoiklivereload import LiveReloader
from sanic import Sanic
from sanic.response import json
from itertools import product

reloader = LiveReloader()
reloader.start_watcher_thread()
app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.delete('/')
async def delete(request):
    return json({'hello': 'world2'})

@app.get('/probability/classic')
async def probabilityClassic(request):
    return request.args.get('m') / request.args.get('n')

def permutationTable(events, repetitions):
    table  = [];
    for x in product(events, repeat=repetitions):
      table.append(''.join(x))
    return table;

@app.get('/permutation')
async def permutation(request):
    #http://rosettacode.org/wiki/Permutations_with_repetitions#Python
    events = request.args.get('events')
    repetitions = int(request.args.get('repetitions'))
    return json({'result': permutationTable(events, repetitions)})

#

@app.get('/probability/event/equal')
async def probabilityEvent(request):
    event = request.args.get('event')
    events = request.args.get('events')
    repetitions = int(request.args.get('repetitions'))
    p = 0;
    for possibility in permutationTable(events, repetitions):
        if (event in possibility):
            p += 1;
    return json({'result': p / number(len(events), repetitions)})

    #event = request.args.get('event')
    #events = request.args.get('events')
    #repetitions = int(request.args.get('repetitions'))
    #space = number(len(events), repetitions)
    #return json({'result': (1/space) * len(event)})


def number(numberEvents, repetitions):
    return numberEvents ** repetitions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
