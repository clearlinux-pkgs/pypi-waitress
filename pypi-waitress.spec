#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-waitress
Version  : 2.1.2
Release  : 93
URL      : https://files.pythonhosted.org/packages/72/83/c3de9799e2305898b02ea67bcd125ad06f271e2a82cc86fe66b7bf4e6f63/waitress-2.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/83/c3de9799e2305898b02ea67bcd125ad06f271e2a82cc86fe66b7bf4e6f63/waitress-2.1.2.tar.gz
Summary  : Waitress WSGI server
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-waitress-bin = %{version}-%{release}
Requires: pypi-waitress-license = %{version}-%{release}
Requires: pypi-waitress-python = %{version}-%{release}
Requires: pypi-waitress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Waitress
========
.. image:: https://img.shields.io/pypi/v/waitress.svg
:target: https://pypi.org/project/waitress/
:alt: latest version of waitress on PyPI

%package bin
Summary: bin components for the pypi-waitress package.
Group: Binaries
Requires: pypi-waitress-license = %{version}-%{release}

%description bin
bin components for the pypi-waitress package.


%package license
Summary: license components for the pypi-waitress package.
Group: Default

%description license
license components for the pypi-waitress package.


%package python
Summary: python components for the pypi-waitress package.
Group: Default
Requires: pypi-waitress-python3 = %{version}-%{release}

%description python
python components for the pypi-waitress package.


%package python3
Summary: python3 components for the pypi-waitress package.
Group: Default
Requires: python3-core
Provides: pypi(waitress)

%description python3
python3 components for the pypi-waitress package.


%prep
%setup -q -n waitress-2.1.2
cd %{_builddir}/waitress-2.1.2
pushd ..
cp -a waitress-2.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362472
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-waitress
cp %{_builddir}/waitress-2.1.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-waitress/a0b53f43aab58b46bf79ba756c50771c605ab4c5
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/waitress-serve

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-waitress/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
