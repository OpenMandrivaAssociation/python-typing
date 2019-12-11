%define module	typing
Name:           python-%{module}
Version:	3.7.4.1
Release:	2
Summary:        Typing defines a standard notation for type annotations
Group:          Development/Python
License:        Python
URL:            https://pypi.python.org/pypi/typing
Source0:	https://files.pythonhosted.org/packages/67/b0/b2ea2bd67bfb80ea5d12a5baa1d12bda002cab3b6c9b48f7708cd40c34bf/typing-3.7.4.1.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python3egg(setuptools)

%description
Typing defines a standard notation for Python function and variable type
annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type checkers, static analyzers, IDEs and other tools.

%package -n python2-%{module}
Summary:	Python2 decorator utilities
Group:		Development/Python
Requires:	python2
 
%description -n python2-%{module}
Typing defines a standard notation for Python function and variable type
annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type checkers, static analyzers, IDEs and other tools.

%prep
%setup -q -c
pwd
mv %{module}-%{version} python2
cp -r python2 python

%build
pushd python2
%py2_build
popd
pushd python
%py3_build
popd

%install
pushd python2
%py2_install
popd
pushd python
%py3_install
popd

%files
%{python_sitelib}/typing*
%{python_sitelib}/__pycache__/typing.*.pyc

%files -n python2-%{module}
%{python2_sitelib}/typing*
