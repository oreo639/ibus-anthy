if get_option('installed_tests')
  foreach file : ['anthytest.py', 'anthycases.py']
    install_data(file, install_dir : get_option('libexecdir') / 'installed-tests' / meson.project_name())
  endforeach
endif

test('Run engine tests', find_program('test-build.sh'), args: ['--builddir='+meson.current_build_dir(), '--srcdir='+meson.current_source_dir()])
