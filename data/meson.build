appdata_file = i18n.merge_file(
  input: 'ibus-anthy.appdata.xml.in',
  output: 'ibus-anthy.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: get_option('datadir') / 'metainfo',
)

schema_conf = configuration_data()
schema_conf.set('KASUMI_EXEC_FILE', kasumi_exec)
schema_conf.set('KASUMI_EXEC_BASENAME', kasumi_exec.split('/')[-1])
schema_conf.set('KASUMI_ICON_FILE', kasumi_icon)
schema_conf.set('ON_OFF_KEYS', get_option('on_off_keys'))
schema_conf.set('pkgdatadir', datadir / meson.project_name())
configure_file(
  input: 'org.freedesktop.ibus.engine.anthy.gschema.xml.in',
  output: 'org.freedesktop.ibus.engine.anthy.gschema.xml',
  configuration: schema_conf,
  install: true,
  install_dir: get_option('datadir') / 'glib-2.0' / 'schemas'
)

emoji_t = custom_target('emoji.t',
  command: [gen_emoji_t, '@INPUT0@', '@INPUT1@', '@OUTPUT@'],
  input: ['emoji-emoji.t', 'emoji-each.t'],
  output: 'emoji.t',
  install: true,
  install_dir: pkgdatadir / 'dicts',
)

anthy_dir = anthy_dep.get_variable(pkgconfig: 'anthydir', default_value: '')
if anthy_dir == ''
  anthy_dir = anthy_dep.get_variable(pkgconfig: 'prefix') / 'share' / anthy_dep.name()
endif

zipcode_t = custom_target('zipcode.t',
  command: [find_program('zipcode-textdic.py'), '@INPUT@', '@OUTPUT@'],
  input: anthy_dir / 'zipcode.t',
  output: 'zipcode.t',
  install: true,
  install_dir: pkgdatadir / 'dicts',
)

install_data('era.t', install_dir : pkgdatadir / 'dicts')
install_data('oldchar.t', install_dir : pkgdatadir / 'dicts')
install_data('symbol.t', install_dir : pkgdatadir / 'dicts')
