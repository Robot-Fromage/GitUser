#:::::::::::::::::::::::::
#::
#:: GitUser/switch.py
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
import subprocess
import os, sys
from colorama import Fore, Back, Style
from colorama import init as init_colorama
init_colorama()

def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out

def command( iArgs, iConfig, iRegistry ):
    if len( iArgs ) > 1:
        print( "Additional arguments were ignored" )

    # Arg parsing
    arg_profile = ""
    if len( iArgs ):
        arg_profile = iArgs[0]

    if not arg_profile in iRegistry:
        print( Fore.RED + "error: profile '{0}' not found".format( arg_profile ) + Style.RESET_ALL )
        sys.exit()

    profile_name    = iRegistry[arg_profile]["name"]
    profile_email   = iRegistry[arg_profile]["email"]
    ret_name    = system( "git", "config", "user.name", profile_name ).decode('utf-8').strip()
    ret_email   = system( "git", "config", "user.email", profile_email ).decode('utf-8').strip()
