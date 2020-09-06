#
# Conditional build:
%bcond_without	tests	# smoke/regression test

Summary:	Python 2 extension to convert files between character sets
Summary(pl.UTF-8):	Rozszerzenie Pythona 2 do konwersji plików między zestawami znaków
Name:		python-recode
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://github.com/pybliographer/python-recode/releases
Source0:	https://github.com/pybliographer/python-recode/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	28e9fc5e0f93c3feb7c5569f5d8b9bf4
Patch0:		%{name}-test.patch
URL:		https://pypi.org/project/recode/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	recode-devel >= 3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a simple binding to GNU Recode, a library to
convert text and files between character sets.

%description -l pl.UTF-8
Ten moduł zawiera proste wiązanie do GNU Recode - biblioteki do
konwersji tekstu i plików między zestawami znaków.

%prep
%setup -q
%patch0 -p1

%build
%py_build

%if %{with tests}
PYTHONPATH=$(echo build-2/lib.*) \
%{__python} testsuite.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%attr(755,root,root) %{py_sitedir}/recode.so
%{py_sitedir}/python_recode-%{version}-py*.egg-info
