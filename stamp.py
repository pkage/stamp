#! /usr/bin/env python

import sys
import os
import shutil
import argparse

# temporary
tdir = "./templates";

# set up argument parser
parser = argparse.ArgumentParser(description="create and save templates from directories");
parser.add_argument("-l", help="list all saved templates", action="count"); 
parser.add_argument("-s", help="create a template from the current directory as <name>", metavar="<name>");
parser.add_argument("-p", help="paste template <name> into the current directory", metavar="<name>");
parser.add_argument("-P", help="same as -p, but overwriting existing files", metavar="<name>");
parser.add_argument("-x", help="delete a template by name", metavar="<name>");

args = parser.parse_args()

templates = os.listdir(tdir);

if (args.l):
    if (len(templates) == 0):
        print("No saved templates.")
    else:
        print("Currently saved templates:");
        for tmp in templates:
            print("     " + tmp);
    sys.exit(0);

if (args.p or args.P): 
    arg = "";
    if args.p and not args.P:
        arg = args.p
    else:
        arg = args.P

    if not arg in templates:
        print("Template \"" + arg + "\" not found.")
        sys.exit(1);

    for obj in os.listdir(os.path.join(tdir, arg)):
        shutil.copy2(os.path.join(tdir, arg, obj), os.getcwd());

    print ("Pasted \"" + arg + "\" successfully");
    sys.exit(0);

if (args.x):
    if not args.x in templates:
        print("Template \"" + args.x + "\" not found.");
        sys.exit(1);

    shutil.rmtree(os.path.join(tdir, args.x));

    print("Removed template \"" + args.x + "\".");
    sys.exit(0);

if (args.s):
    if args.x in templates:
        print("Template \"" + args.s + "\" exists, avoiding overwrite.");
        sys.exit(1);

    os.mkdir(os.path.join(tdir, args.s));

    for obj in os.listdir(os.getcwd()):
        print("will copy " + obj);
        shutil.copy2(os.path.join(os.getcwd(), obj), os.path.join(tdir, args.s));
    
    print("Created template \"" + args.s + "\" successfully.");
    sys.exit(0);
