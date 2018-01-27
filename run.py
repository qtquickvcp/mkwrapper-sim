#!/usr/bin/python

import sys
import os
import subprocess
import argparse
import time
from machinekit import launcher

os.chdir(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser(description='This is the motorctrl demo run script '
                                 'it demonstrates how a run script could look like '
                                 'and of course starts the motorctrl demo')
parser.add_argument('-s', '--halscope', help='Starts the halscope', action='store_true')
parser.add_argument('-m', '--halmeter', help='Starts the halmeter', action='store_true')
parser.add_argument('-p', '--path', help='Adds an additional UI search path to configserver')
parser.add_argument('-l', '--lathe', help='Enables the lathe simulator config', action='store_true')
parser.add_argument('-d', '--debug', help='Enable debug mode', action='store_true')

args = parser.parse_args()

if args.debug:
    launcher.set_debug_level(5)

try:
    launcher.check_installation()
    launcher.cleanup_session()
    launcher.register_exit_handler()  # needs to executed after HAL files

    nc_path = os.path.expanduser('~/nc_files')
    if not os.path.exists(nc_path):
        os.mkdir(nc_path)

    launcher.ensure_mklauncher()

    # the point-of-contact for QtQUickVCP
    launcher.start_process('configserver -n mkwrapper-Demo . ~/projects/Machineface ~/projects/Cetus %s' % args.path)

    # start machinekit
    if not args.lathe:
        launcher.start_process('machinekit mkwrapper.ini')
    else:
        launcher.start_process('machinekit lathe.ini')

    if args.halscope:
        # load scope only now - because all sigs are now defined:
        launcher.start_process('halscope')
    if args.halmeter:
        launcher.start_process('halmeter')

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

sys.exit(0)
