#:::::::::::::::::::::::::
#::
#:: GitUser.py
#::_______________________
#::
#:: Author: Clement BERTHAUD
#::
#:: MIT License
#:: Copyright (c) 2018 GitUser - Clément BERTHAUD
#::
#:: Permission is hereby granted, free of charge, to any person obtaining a copy
#:: of this software and associated documentation files (the "Software"), to deal
#:: in the Software without restriction, including without limitation the rights
#:: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#:: copies of the Software, and to permit persons to whom the Software is
#:: furnished to do so, subject to the following conditions:
#::
#:: The above copyright notice and this permission notice shall be included in all
#:: copies or substantial portions of the Software.
#::
#:: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#:: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#:: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#:: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#:: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#:: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#:: SOFTWARE.
#::
#:::::::::::::::::::::::::
import sys, os, json
from colorama import Fore, Back, Style
from colorama import init as init_colorama
init_colorama()

working_dir = os.getcwd()
script_dir = os.path.dirname( os.path.realpath( __file__ ) ).replace( os.sep, '/' ) + '/'
sys.path.append( script_dir )

registry_file_name  = script_dir + ".registry"
config_file_name    = script_dir + ".config"

if not os.path.exists( registry_file_name ):
    print( Fore.RED + "error: '.registry' not found" + Style.RESET_ALL )
    sys.exit()

if not os.path.exists( config_file_name ):
    print( Fore.RED + "error: '.config' not found" + Style.RESET_ALL )
    sys.exit()

registry_file   = open( registry_file_name )
registry_data   = json.load( registry_file )
config_file     = open( config_file_name )
config_data     = json.load( config_file )

# Gather commands
modules  = {}
commands = {}
for entry in config_data["keys"]: modules[ entry["name"]] = __import__( "GitUser." + entry["name"], fromlist=[ "GitUser" ] )
for entry in config_data["keys"]: commands[entry["name"]] = getattr( modules[entry["name"]], "command" )

# Parse args
command = ""
args    = []
if len( sys.argv ) > 1:
    command = sys.argv[1]   # Gather command
    args    = sys.argv[2:]  # Gather args

# Exec
for entry in config_data["keys"]:
    if command == entry["name"] or command == entry["alias"]:
        commands[ entry["name"] ]( args, config_data, registry_data )
        sys.exit()

print( "error:" + "'" + command + "'" + " is not a valid command. See 'GitUser help'")
