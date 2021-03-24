# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_imports = ['jsonlines', 'websockets', 'minecraft_learns', 'flask']

added_files = [('back_end\*.py', 'back_end'), 
    ('front_end', 'front_end')
]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\carlo\\Documents\\GitHub\\Minecraft_AI\\src', 'C:\\Users\\carlo\\AppData\\Local\\Programs\\Python'],
             binaries=[],
             datas=added_files,
             hiddenimports=added_imports,
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
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='main')