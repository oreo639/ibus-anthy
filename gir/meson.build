libanthygobject_deps = [
  anthy_dep,
  dependency('gobject-2.0', version: glib_required_version),
]

libanthygobject = library('anthygobject-1.0',
  sources: ['anthygcontext.c'],
  dependencies: libanthygobject_deps,
  version: '5.0.0',
  install: true,
)

install_headers('anthygcontext.h', subdir: meson.project_name()+'-1.0')

anthygobject_dep = declare_dependency(
  link_with: libanthygobject,
  dependencies: libanthygobject_deps,
)

# Find location of anthy header for GIR
# Use cflags from pkg-config to get header location when cross-compiling and fallback
# and fallback to includedir if no cflags are provided.
found = false
anthy_cflags = run_command(pkgconfig_prog, '--cflags', anthy_dep.name(), check: true).stdout().strip().split()
anthy_cflags += '-I'+anthy_dep.get_variable(pkgconfig: 'includedir')
foreach cflag : anthy_cflags
  if not found and cflag.startswith('-I')
    cflag = cflag.strip('-I')
    try_header = cflag / 'anthy/anthy.h'
    if fs.is_file(try_header)
      anthy_header = try_header
      found = true
    endif
  endif
endforeach
if not found
  error('Could not find anthy header. Tried '+' '.join(anthy_cflags))
endif

gnome.generate_gir(libanthygobject,
  nsversion: '9000',
  namespace: 'Anthy',
  symbol_prefix: 'anthy',
  identifier_prefix: 'Anthy',
  includes: 'GObject-2.0',
  sources: ['anthygcontext.c', 'anthygcontext.h', anthy_header],
  dependencies: [anthy_dep],
  extra_args: ['--accept-unprefixed'],
  export_packages: anthy_dep.name(),
  install: true,
)

anthygcontext_test = executable('anthygcontext_test',
  sources: 'test.c',
  dependencies: [anthygobject_dep],
)

test('libanthygobject tests', anthygcontext_test)
