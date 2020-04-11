# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['../src/main.py'],
             pathex=['/Users/russellslighton/Documents/princeton/thesis/Elevator-ad-Parnassum/release'],
             binaries=[('/usr/local/Cellar/z3/4.8.7/lib/libz3.dylib', '.')],
             datas=[],
             hiddenimports=['z3-solver', 'scikit-learn'],
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
          name='SM(Bach)',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='../rec/smb.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SM(Bach)')
app = BUNDLE(coll,
             name='SM(Bach).app',
             icon='../rec/smb.icns',
             bundle_identifier=None,
             info_plist={
                 'NSPrincipalClass': 'NSApplication'
             }
        )
