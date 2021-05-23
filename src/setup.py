from distutils.core import setup, Extension

elas = Extension('elas', sources=[
    'pyelas.cpp',
    'elas.cpp',
    'descriptor.cpp',
    'filter.cpp',
    'matrix.cpp',
    'triangle.cpp',
    ], define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')])

setup(name='elas',
      version='1.0',
      description='These are the Python bindings for Libelas.',
      ext_modules=[elas])
