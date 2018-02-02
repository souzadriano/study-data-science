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

@app.get('/permutation')
async def permutation(request):
    #http://rosettacode.org/wiki/Permutations_with_repetitions#Python
    table  = [];
    print(request.args.get('s'))
    for x in product('ACRK', repeat=5):
      table.append(''.join(x))
    return json({'result': table, "json": request.raw_args})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
