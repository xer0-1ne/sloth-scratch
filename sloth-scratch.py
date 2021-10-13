#!/usr/bin/env python3
import json
from assets.lib.bottle import route, run, static_file, response, request, redirect

#get default routes for files/paths
@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root="./")

#route index as default page
@route('/')
def index():
    filename='index.html'
    return static_file(filename, root="./")

#return json object
@route('/commands')
def getCommands():
    objFile = 'commands.json'
    response.content_type = 'application/json'

    with open(objFile, "r") as file:
        data = json.load(file)
        return json.dumps(data)

@route('/addcommand', method="POST")
def addCommands():
    command = request.forms.get('newCommand')
    commandName = request.forms.get('newCommandName')
    commandOS = request.forms.get('newCommandOS')
    commandDescription = request.forms.get('newCommandDescription')

    commandObj = {
        "Command":command,
        "Name":commandName,
        "OS":commandOS,
        "Description":commandDescription
    }

    objFile = 'commands.json'
    response.content_type = 'application/json'

    with open(objFile, "r") as file:
        data = json.load(file)

    data.append(commandObj)

    with open(objFile, "w") as file:
        json.dump(data, file)
   
    redirect('/')

run(host='localhost', port=8080, debug=True, reloader=True)
