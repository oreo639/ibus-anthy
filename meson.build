project('ibus-anthy',
  ['c'],
  version: '1.5.15',
  license: 'LGPL2.1+',
  meson_version: '>= 0.56',
)

i18n = import('i18n')
gnome = import('gnome')
python = import('python')
fs = import('fs')

prefix = get_option('prefix')
bindir = prefix / get_option('bindir')
datadir = prefix / get_option('datadir')
libdir = prefix / get_option('libdir')
includedir = prefix / get_option('includedir')
libexecdir = prefix / get_option('libexecdir')
sysconfdir = prefix / get_option('sysconfdir')
localedir = prefix / get_option('localedir')
pkgdatadir = datadir / meson.project_name()

ibus_required_version='1.5.0'
glib_required_version='>=2.26.0'

cc = meson.get_compiler('c')

py_installation = python.find_installation(get_option('python'))
gen_emoji_t = find_program('build-aux/meson/gen_emoji_t.py')
pkgconfig_prog = find_program('pkg-config')
anthy_dep = dependency('anthy-unicode', fallback: ['anthy'], required: true)

config_h = configuration_data()
config_h.set('VERSION', '"'+meson.project_version()+'"')
config_h.set('PACKAGE', '"'+meson.project_name()+'"')
config_h.set('GETTEXT_PACKAGE', meson.project_name())
foreach a : ['NTH_UNCONVERTED_CANDIDATE', 'NTH_KATAKANA_CANDIDATE', 'NTH_HIRAGANA_CANDIDATE', 'NTH_HALFKANA_CANDIDATE']
  if cc.has_header_symbol('anthy/anthy.h', a, dependencies: anthy_dep)
    config_h.set('HAVE_'+a.to_upper(), 1,
      description: 'Define to 1 if you have the declaration of `'+a+'\', and to 0 if you don\'t.')
  endif
endforeach
configure_file(output: 'config.h', configuration: config_h)

kasumi_exec = get_option('kasumi_exec')
if kasumi_exec == ''
  kasumi_exec = bindir / 'kasumi'
endif
kasumi_icon = get_option('kasumi_icon')
if kasumi_icon == ''
  kasumi_icon = datadir / 'pixmaps' / 'kasumi.png'
endif

if get_option('hotkeys') == 'no'
  hotkeys_xml = '<!-- <hotkeys>Control+space,Zenkaku_Hankaku</hotkeys> -->'
elif get_option('hotkeys') == 'yes' or get_option('hotkeys') == ''
  hotkeys_xml = '<hotkeys>Control+space,Zenkaku_Hankaku</hotkeys>'
elif get_option('hotkeys') == 'null'
  hotkeys_xml = '<hotkeys></hotkeys>'
else
  hotkeys_xml = '<hotkeys>'+get_option('hotkeys')+'</hotkeys>'
endif

layout_xml = '<layout>'+get_option('keylayout')+'</layout>'
symbol_char='&#x3042;'
symbol_char_int='0x3042'
symbol_xml='<symbol>'+symbol_char+'</symbol>'
icon_prop_key_xml='<icon_prop_key>InputMode</icon_prop_key>'

# Sanity checks
ibus_check_version='''
from gi.repository import IBus
def _ibus_check_version(v):
    major = IBus.MAJOR_VERSION
    minor = IBus.MINOR_VERSION
    micro = IBus.MICRO_VERSION
    if (major, minor, micro) < tuple(map(int, (v.split('.')))):
        raise ValueError('Required ibus %s but version of ibus is %d.%d.%d' % \
                         (v, major, minor, micro))

_ibus_check_version('@0@')
'''.format(ibus_required_version)
r=run_command(py_installation, '-c', ibus_check_version, env: 'PYTHONWARNINGS=ignore', check: false)
if r.returncode() != 0
  error(r.stderr())
endif

ibus_check_enginesym='from gi.repository import IBus;exit(not hasattr(IBus.EngineDesc, \'get_symbol\'))'
if run_command(py_installation, '-c', ibus_check_enginesym, check: false).returncode() != 0
  error('ibus version 1.4.0 or later should support symbol in IBus.EngineDesc')
endif

ibus_check_propertysym='from gi.repository import IBus;exit(not hasattr(IBus.Property, \'get_symbol\'))'
if run_command(py_installation, '-c', ibus_check_propertysym, check: false).returncode() != 0
  error('ibus version 1.5.0 or later should support symbol in IBus.Property')
endif

ibus_check_enginelayopt='from gi.repository import IBus;exit(not hasattr(IBus.EngineDesc, \'get_layout_option\'))'
if run_command(py_installation, '-c', ibus_check_enginelayopt, check: false).returncode() != 0
  error('ibus version 1.5.0 or later should support layout_option in IBus.EngineDesc')
endif

ibus_check_engineversion='from gi.repository import IBus;exit(not hasattr(IBus.EngineDesc, \'get_version\'))'
if run_command(py_installation, '-c', ibus_check_engineversion, check: false).returncode() != 0
  error('ibus version 1.5.0 or later should support version in IBus.EngineDesc')
endif

ibus_check_enginepropkey='from gi.repository import IBus;exit(not hasattr(IBus.EngineDesc, \'get_icon_prop_key\'))'
if run_command(py_installation, '-c', ibus_check_enginepropkey, check: false).returncode() != 0
  icon_prop_key_xml='<!-- '+icon_prop_key_xml+' -->'
  warning('ibus 1.5.11 or later supports icon-prop-key in IBus.EngineDesc')
endif

subdir('po')
subdir('data')
subdir('icons')
subdir('gir')
subdir('engine')
subdir('setup')
subdir('tests')

summary({
    'prefix': prefix,
    'libdir': libdir,
    'datadir': datadir,
    'bindir': bindir,
  },
  section: 'Directories',
)

summary({
    'Optimization': get_option('optimization'),
    'Kasumi': kasumi_exec,
    'Kasumi icon': kasumi_icon,
    'Preference icon': get_option('icon_preference'),
    'On-off-keys': get_option('on_off_keys'),
    'Layout': get_option('keylayout'),
    'Pygtk2': get_option('pygtk2_anthy')
  },
  section: 'Build',
)
