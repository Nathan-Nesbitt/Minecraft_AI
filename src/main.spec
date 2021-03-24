# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [('back_end\*.py', 'back_end'), 
    ('front_end*.py', 'front_end'), 
    ('front_end\templates\*.html', 'front_end\templates'), 
    ('front_end\templates\lessons\*.md', 'front_end\templates\lessons'), 
    ('front_end\static\setup\*.js', 'front_end\static\setup'), 
    ('front_end\static\includes\*.jpg', 'front_end\static\includes'), 
    ('front_end\static\includes\*.png', 'front_end\static\includes'), 
    ('front_end\static\includes\*.jfif', 'front_end\static\includes'), 
    ('front_end\static\includes\*.ttf', 'front_end\static\includes'), 
    ('front_end\static\css\*.css', 'front_end\static\css'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\js\*.js', 'front_end\static\css\bootstrap-3.3.7-dist\js'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\fonts\*.eot', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\fonts\*.svg', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\fonts\*.ttf', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\fonts\*.woff', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\fonts\*.woff2', 'front_end\static\css\bootstrap-3.3.7-dist\fonts'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\css\*.css', 'front_end\static\css\bootstrap-3.3.7-dist\css'), 
    ('front_end\static\css\bootstrap-3.3.7-dist\css\*.map', 'front_end\static\css\bootstrap-3.3.7-dist\css')
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
