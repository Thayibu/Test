# -*- mode: python ; coding: utf-8 -*-
# Import Kivy dependency bins
from kivy_deps import sdl2, glew, angle
import os
block_cipher = None

def safe_bins(dep_bins):
    return [(f, ".") for f in dep_bins if f]
project_path = os.path.abspath(".")

a = Analysis(
    ['main.py'],  
    pathex=["."],
    binaries=safe_bins(angle.dep_bins) + safe_bins(sdl2.dep_bins) + safe_bins(glew.dep_bins),
    datas=[
        ('001.png', '.'),
        ('002.png', '.'),
        ('003.png', '.'),
        ('004.png', '.'),
        ('Delivery.jpg', '.'),
        ('frame.png', '.'),
        ('headlight_off.png', '.'),
        ('headlight_on.png', '.'),
        #('icon_path', '.'),
        ('icon.png', '.'),
        ('KLK.jpg', '.'),
        ('Photo 1.png', '.'),
        ('Photo 2.png', '.'),
        ('Photo 3.jpg', '.'),
        ('Photo-4.png', '.'),
        ('presplash.png', '.'),
        ('PSM (Phone).jpg', '.'),
        ('PSM.txt', '.'),
        ('records.txt', '.'),
        ('Register.txt', '.'),
        ('Show.jpg', '.'),
    ],
    hiddenimports=['pandas',
            'kivy_deps.sdl2',
            'kivy_deps.glew',
            'kivy_deps.angle',
            'kivymd',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    hooksconfig={},
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PSM_Hyundai',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    #icon=icon_path
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PSM_Hyundai'
)
