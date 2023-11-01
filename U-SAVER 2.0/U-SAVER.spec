# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/U-SAVER (DT-PROJECT group 8 SEM1)/U-SAVER.py'],
             pathex=[],
             binaries=[],
             datas=[('D:/U-SAVER (DT-PROJECT group 8 SEM1)/az_dark.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/az_light.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/f_dark.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/Logo.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/logo_Dark.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/logo_icon.ico', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/logo_Light.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/mic_2.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/mic_logo.png', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/sv.tcl', '.'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/theme', 'theme/'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/Forest', 'Forest/'), ('D:/U-SAVER (DT-PROJECT group 8 SEM1)/Azure-ttk-theme-main', 'Azure-ttk-theme-main/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='U-SAVER',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='D:\\U-SAVER (DT-PROJECT group 8 SEM1)\\logo_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='U-SAVER')
