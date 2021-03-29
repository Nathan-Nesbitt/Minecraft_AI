# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)

from PyInstaller.utils.hooks import collect_submodules

hidden_imports = collect_submodules('sklearn')
hidden_imports.append('json')
hidden_imports.append('websockets')
hidden_imports.append('asyncio')

added_files = [('back_end', 'back_end'), 
    ('front_end', 'front_end')
]

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\carlo\\Desktop\\ve_MC\\Minecraft_AI\\src', 'C:\\Users\\carlo\\Desktop\\ve_MC\\Minecraft_AI\\venv\\Lib', 'C:\\Users\\carlo\\Desktop\\ve_MC\\Minecraft_AI\\venv\\Scripts'],
             binaries=[],
             datas=added_files,
             hiddenimports=hidden_imports,
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

coll = COLLECT(exe,
               a.scripts,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='main')