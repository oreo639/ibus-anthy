inputmethod_conf = configuration_data()
inputmethod_conf.set('LAYOUT_XML', layout_xml)
inputmethod_conf.set('HOTKEYS_XML', hotkeys_xml)
inputmethod_conf.set('SYMBOL_XML', symbol_xml)
inputmethod_conf.set('ICON_PROP_KEY_XML', icon_prop_key_xml)
inputmethod_conf.set('PACKAGE_VERSION', meson.project_version())
inputmethod_conf.set('PACKAGE', meson.project_name())
inputmethod_conf.set('PKGDATADIR', pkgdatadir)
inputmethod_conf.set('LIBEXECDIR', libexecdir)
configure_file(
  input: 'default.inputMethod.xml.in.in',
  output: 'default.xml',
  configuration: inputmethod_conf,
  install: true,
  install_dir: pkgdatadir / 'engine'
)
configure_file(
  input: 'anthy.inputMethod.xml.in.in',
  output: 'anthy.xml',
  configuration: inputmethod_conf,
  install: true,
  install_dir: get_option('datadir') / 'ibus'/ 'component'
)

engine_sources = [
  'engine.py',
  'factory.py',
  'jastring.py',
  'kana.py',
  'main.py',
  'romaji.py',
  'segment.py',
  'tables.py',
  'thumb.py',
]

if get_option('pygtk2_anthy')
  swig = find_program('swig', required: true)
  python_dep = py_installation.dependency()
  pkgconfig_prog = find_program('pkg-config')
  anthy_cflags = run_command(pkgconfig_prog, '--cflags', anthy_dep.name(), check: true).stdout().strip()
  python_cflags = run_command(pkgconfig_prog, '--cflags', python_dep.name(), check: true).stdout().strip()
  swig_files = custom_target('[anthy.py|anthy_wrap.c]',
    command: [swig, '-python', anthy_cflags, python_cflags, '-o', '@OUTPUT1@', '@INPUT0@'],
    input: ['anthy.i'],
    output: ['anthy.py', 'anthy_wrap.c'],
    install: true,
    install_dir: [pkgdatadir / 'engine', false],
  )
  py_installation.extension_module('_anthy',
    sources: [swig_files[1]],
    dependencies: [anthy_dep],
    install: true,
    install_dir: pkgdatadir / 'engine',
  )
endif

engine_conf = configuration_data()
engine_conf.set('pkgdatadir', datadir / meson.project_name())
engine_conf.set('libexecdir', libexecdir)
engine_conf.set('datadir', datadir)
engine_conf.set('ANTHY_PC', anthy_dep.name())
engine_conf.set('VERSION', meson.project_version())
engine_conf.set('LAYOUT', get_option('keylayout'))
engine_conf.set('SYMBOL_CHAR_INT', symbol_char_int)
engine_conf.set('ICON_PREFERENCE', get_option('icon_preference'))
engine_sources += configure_file(
  input: '_config.py.in',
  output: '_config.py',
  configuration: engine_conf,
)

foreach file : engine_sources
  install_data(file, install_dir : pkgdatadir / 'engine')
endforeach

ibus_engine_anthy_conf = configuration_data()
ibus_engine_anthy_conf.set('prefix', prefix)
ibus_engine_anthy_conf.set('datarootdir', datadir)
ibus_engine_anthy_conf.set('libexecdir', libexecdir)
ibus_engine_anthy_conf.set('PACKAGE', meson.project_name())
ibus_engine_anthy_conf.set('PYTHON', get_option('python'))
ibus_engine_anthy_conf.set('ENV_IBUS_ENGINE', get_option('engine_env'))
configure_file(
  input: 'ibus-engine-anthy.in',
  output: 'ibus-engine-anthy',
  configuration: ibus_engine_anthy_conf,
  install: true,
  install_dir: get_option('libexecdir'),
  install_mode: 'rwxr-xr-x',
)
