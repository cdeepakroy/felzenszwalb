from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy

setup(
    packages = ['felzenszwalb'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("felzenszwalb.ccomp", ["felzenszwalb/ccomp.pyx"]),
                   Extension("felzenszwalb._felzenszwalb_cy", ["felzenszwalb/_felzenszwalb_cy.pyx"])],
    include_dirs = ['src', numpy.get_include()]
)
