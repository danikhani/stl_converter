# stl_converter
Python file that uses Blender to convert .stl to .obj and .ply

# Prerequesities
1. Install blender.
      ```bash
    sudo apt-get install blender
   ```
2. Create virtual environment.
      ```bash
    conda create -n stl_converter python=3.8
   ```
3. Activate environment: 
      ```bash
    conda activate stl_converter
   ```
3. Install blender-python api using conda: 
   ```bash
     conda install -c kitsune.one python-blender
   ```

# Run Code
1. Change to directory where main.py is located.
2. Add the stl files to a folder (for example stl_folder)
2. In terminal run: blender --background --python main.py -- <folder_path_of_stl_files> <folder_path_of_saving>
example: 
   ```bash
    blender --background --python main.py -- stl_folder export_folder
   ```

  
# Settings
It is possible to change coordinates of the objects coordinate system. See blender docs for more information. 
https://docs.blender.org/api/current/bpy.ops.export_scene.html
https://docs.blender.org/api/current/bpy.ops.export_mesh.html

