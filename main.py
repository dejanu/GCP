import json
from bottle import run,get,post,request,Bottle
##basic API

app = Bottle()

commands  = [{"name":"run", "description":"docker run -it IMAGE :create container and keept STDIN open and allocate tty"},
             {"name":"exec", "description":"docker exec -it CONTAINER : Open interactive tty to running container"},
             {"name":"start", "description":"docker start -ai CONTAINER : Attach interactive tty to running container"},
             ]


@app.route('/')
def hello():
    return "<h3>Bottle API<//h3><br>API commands: command command//name "

@app.get('/commands')
def getAll():
    """return json response with all commands in dict"""
    return{'dockercommands':commands}

@app.get('/command/<name>/')
def getCommand(name):
    """return a certain command"""
    #list with dict which has the hey name == with GET param from URL
    the_command = [ i for i in commands if i["name"]== name]
    return {'command':the_command[0]}


@app.post('/newcommand')
def addCommand():
    new_command = {'name':request.json.get('name'),'description':request.json.get('description')}
    commands.append(new_command)
    return {'commands':commands}

##if __name__ == "__main__":
##    run(app,ost="localhost",port=8080,reloader=True,debug=True)
