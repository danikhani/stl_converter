'''
This code automates the converting-process from .stl to .obj and .ply.

Run in terminal: blender --background --this_file.py -- filename.stl filename_converted.obj filename_converted.ply

'''

import bpy
import argparse
import os
import utils.util as util


def parse_input():
    parser = argparse.ArgumentParser(description='STL convertor')

    parser.add_argument('-l','--load-path', type=str, help='Path to load the stl files (ie. stl)',required=True)
    parser.add_argument('-s','--save-path', type=str, help='Path to export the files (ie. export)',required=True)

    args = parser.parse_args()
    return args

def main():
    args = parse_input()

    stl_folder = args.load_path
    export = args.save_path

    ply_folder = os.path.join(export, 'ply')
    fbx_folder = os.path.join(export, 'fbx')

    #make folders
    util.make_folder(export)
    util.make_folder(ply_folder)
    util.make_folder(fbx_folder)


    # Delete existing objects in case they exist.
    try:
        objs = bpy.data.objects
        objs.remove(objs["Cube"], do_unlink=True)
        objs.remove(objs["Camera"], do_unlink=True)
        objs.remove(objs["Lamp"], do_unlink=True)

        # delete objects
        bpy.ops.object.delete()
    except:
        pass

    bpy.ops.import_mesh.stl(filepath=stl_folder, axis_forward='Y', axis_up='Z')     # import .stl
    bpy.ops.export_scene.fbx(filepath=fbx_folder, use_blen_objects=True)           # export .fbx
    bpy.ops.export_mesh.ply(filepath=ply_folder, axis_forward='Y', axis_up='Z')    # export .ply


if __name__ == "__main__":
    main()