setup_sources = [
  'anthyprefs.py',
  'main.py',
  'prefs.py',
  'setup.ui',
]

setup_conf = configuration_data()
setup_conf.set('pkgdatadir', datadir / meson.project_name())
setup_conf.set('libexecdir', libexecdir)
setup_conf.set('datadir', datadir)
setup_conf.set('ANTHY_PC', anthy_dep.name())
setup_conf.set('VERSION', meson.project_version())
setup_conf.set('LAYOUT', get_option('keylayout'))
setup_conf.set('SYMBOL_CHAR_INT', symbol_char_int)
setup_conf.set('ICON_PREFERENCE', get_option('icon_preference'))
setup_sources += configure_file(
  input: '_config.py.in',
  output: '_config.py',
  configuration: setup_conf,
)

foreach file : setup_sources
  install_data(file, install_dir : pkgdatadir / 'setup')
endforeach

ibus_setup_anthy_conf = configuration_data()
ibus_setup_anthy_conf.set('prefix', prefix)
ibus_setup_anthy_conf.set('datarootdir', datadir)
ibus_setup_anthy_conf.set('libexecdir', libexecdir)
ibus_setup_anthy_conf.set('localedir', localedir)
ibus_setup_anthy_conf.set('PACKAGE', meson.project_name())
ibus_setup_anthy_conf.set('PYTHON', get_option('python'))
ibus_setup_anthy_conf.set('ENV_IBUS_ENGINE', get_option('engine_env'))
configure_file(
  input: 'ibus-setup-anthy.in',
  output: 'ibus-setup-anthy',
  configuration: ibus_setup_anthy_conf,
  install: true,
  install_dir: get_option('libexecdir'),
  install_mode: 'rwxr-xr-x',
)

ibus_setup_desktop_conf = configuration_data()
ibus_setup_desktop_conf.set('libexecdir', libexecdir)
configure_file(
  input: 'ibus-setup-anthy.desktop.in.in',
  output: 'ibus-setup-anthy.desktop',
  configuration: ibus_setup_desktop_conf,
  install: true,
  install_dir: get_option('datadir') / 'applications',
)
