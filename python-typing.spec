%define module	typing
Name:           python-%{module}
Version:	3.7.4.3
Release:	1
Summary:        Typing defines a standard notation for type annotations
Group:          Development/Python
License:        Python
URL:            https://pypi.python.org/pypi/typing
Source0:	https://files.pythonhosted.org/packages/05/d9/6eebe19d46bd05360c9a9aae822e67a80f9242aabbfc58b641b957546607/typing-3.7.4.3.tar.gz
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
