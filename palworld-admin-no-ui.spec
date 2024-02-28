# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['palworld_admin\\main.py'],
    pathex=[r'C:\palworld-admin-github'],
    binaries=[],
    datas=[
        (r'C:\palworld-admin-github\palworld_admin\migrations', 'migrations'),
        (r'C:\palworld-admin-github\palworld_admin\website\resources', 'resources')
    ],
    hiddenimports=[
        'eventlet',
        'eventlet.hubs.epolls',
        'eventlet.hubs.kqueue',
        'eventlet.hubs.selects',
        'dns',
        'dns.rdtypes',
        'dns.rdtypes.ANY',
        'dns.rdtypes.IN',
        'dns.rdtypes.CH',
        'dns.rdtypes.dnskeybase',
        'dns.asyncbackend',
        'dns.dnssec',
        'dns.e164',
        'dns.namedict',
        'dns.tsigkeyring',
        'dns.versioned',
        'logging.config',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='palworld-admin-no-ui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
