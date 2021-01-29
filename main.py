'''
This code automates the converting-process from .stl to .obj and .ply.

'''


import os
import shutil
import bpy
import sys


def make_folder(folder):
    try:
        shutil.rmtree(folder)
        os.mkdir(folder)
    except FileNotFoundError:
        os.mkdir(folder)
    return folder

def convert_stl_with_blender(file_name, stl_folder, ply_folder, fbx_folder):
    ply_name = file_name.replace('stl', 'ply')
    fbx_name = file_name.replace('stl', 'fbx')
    # save paths
    stl_file = os.path.join(stl_folder, file_name)
    ply_file = os.path.join(ply_folder, ply_name)
    fbx_file = os.path.join(fbx_folder, fbx_name)

    #bpy.ops.wm.read_factory_settings(use_empty=True)
    objs = bpy.data.objects
    try:
        objs.remove(objs["Cube"], do_unlink=True)
    except:
        pass
    try:
        objs.remove(objs["Camera"], do_unlink=True)
    except:
        pass
    try:
        objs.remove(objs["Lamp"], do_unlink=True)
    except:
        pass
    # delete objects
    try:
        bpy.ops.object.delete()
    except:
        pass

    bpy.ops.import_mesh.stl(filepath=stl_file, axis_forward='Y', axis_up='Z')  # import .stl
    # Delete existing objects in case they exist.
    bpy.ops.export_scene.fbx(filepath=fbx_file, axis_forward='Y', axis_up='Z',embed_textures=True,global_scale=0.1)  # export .fbx
    bpy.ops.export_mesh.ply(filepath=ply_file, axis_forward='Y', axis_up='Z',global_scale=0.1)  # export .ply

#not working
def convert_obj_with_blender(file_name, obj_folder, ply_folder, fbx_folder):
    pure_file_name = file_name.replace('.obj', '')
    mat_file_name = file_name.replace('obj', 'mat')
    ply_name = file_name.replace('obj', 'ply')
    fbx_name = file_name.replace('obj', 'fbx')
    # save paths
    obj_file = os.path.join(obj_folder, file_name)
    mat_file = os.path.join(obj_folder, mat_file_name)
    ply_file = os.path.join(ply_folder, ply_name)
    fbx_file = os.path.join(fbx_folder, fbx_name)

    # assignment
    #objs = bpy.data.objects[pure_file_name]

    bpy.ops.import_scene.obj(filepath=obj_file, axis_forward='Y', axis_up='Z')
    obj_objects = bpy.context.selected_objects[:]

    for obj in obj_objects:
        # print the name of the current obj
        print(obj.name)

        # set current object to the active one
        bpy.context.scene.objects.active = obj
        obj.data.materials.append(mat_file)

    #bpy.ops.wm.read_factory_settings(use_empty=True)
    #objs = bpy.data.objects
    '''
    try:
        objs.remove(objs["Cube"], do_unlink=True)
    except:
        pass
    try:
        objs.remove(objs["Camera"], do_unlink=True)
    except:
        pass
    try:
        objs.remove(objs["Lamp"], do_unlink=True)
    except:
        pass
    # delete objects
    try:
        bpy.ops.object.delete()
    except:
        pass'''

    #bpy.ops.import_mesh.stl(filepath=stl_file, axis_forward='Y', axis_up='Z')  # import .stl

    # append material

    # Delete existing objects in case they exist.
    bpy.ops.export_scene.fbx(filepath=fbx_file, axis_forward='Y', axis_up='Z',embed_textures=True)  # export .fbx
    bpy.ops.export_mesh.ply(filepath=ply_file, axis_forward='Y', axis_up='Z')  # export .ply



def main():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--". +1 because argv[0] is code-filepath

    stl_in = argv[0]  # filepath of .stl
    obj_out = argv[1]  # filepath to export .obj

    stl_folder = stl_in
    export = obj_out

    ply_folder = os.path.join(export, 'ply')
    fbx_folder = os.path.join(export, 'fbx')

    #make folders
    make_folder(export)
    make_folder(ply_folder)
    make_folder(fbx_folder)

    list_of_files = os.listdir(stl_folder)

    for data_name in list_of_files:
        # find mask data
        if data_name.endswith('.stl'):
            convert_stl_with_blender(data_name, stl_folder, ply_folder, fbx_folder)
        #if data_name.endswith('.obj'):
            #convert_obj_with_blender(data_name, stl_folder, ply_folder, fbx_folder)


if __name__ == "__main__":
    main()