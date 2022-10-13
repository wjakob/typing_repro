import sys, re, os

try:
    from skbuild import setup
    import nanobind
except ImportError:
    print("The preferred way to invoke 'setup.py' is via pip, as in 'pip "
          "install .'. If you wish to run the setup script directly, you must "
          "first install the build dependencies listed in pyproject.toml!",
          file=sys.stderr)
    raise

setup(
    name="typing_repro",
    version="0.0.1",
    author="Wenzel Jakob",
    author_email="wenzel.jakob@epfl.ch",
    description="An example minimal project that compiles bindings using nanobind and scikit-build",
    url="https://github.com/wjakob/typing_repro",
    license="BSD",
    packages=['typing_repro'],
    package_dir={'': 'src'},
    cmake_install_dir="src/typing_repro",
    include_package_data=True,
    python_requires=">=3.8"
)
