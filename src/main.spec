# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [('src\back_end\*.py', 'back_end'), ('\front_end*.py', 'front_end'), 
    ('src\front_end\templates\*.html', 'front_end\templates'), 
    ('src\front_end\templates\lessons\*.md', 'front_end\templates\lessons'), 
    ('src\front_end\static\setup\*.js', 'front_end\static\setup'), 
    ('src\front_end\static\includes\*.jpg', 'front_end\static\includes'), 
    ('src\front_end\static\includes\*.png', 'front_end\static\includes'), 
    ('src\front_end\static\includes\*.jfif', 'front_end\static\includes'), 
    ('src\front_end\static\includes\*.ttf', 'front_end\static\includes'), 
    ('src\front_end\static\css\*.css', 'front_end\static\css'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\js\*.js', 'front_end\static\css\bootstrap-3.3.7-dist\js'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\fonts\*.eot', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\fonts\*.svg', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\fonts\*.ttf', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\fonts\*.woff', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\fonts\*.woff2', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\css\*.css', 'front_end\static\css\bootstrap-3.3.7-dist\css'), 
    ('src\front_end\static\css\bootstrap-3.3.7-dist\css\*.map', 'front_end\static\css\bootstrap-3.3.7-dist\css')
]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\carlo\\Documents\\GitHub\\Minecraft_AI\\src'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
