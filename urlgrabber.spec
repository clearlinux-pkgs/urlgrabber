#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urlgrabber
Version  : 3.10.2
Release  : 26
URL      : http://urlgrabber.baseurl.org/download/urlgrabber-3.10.2.tar.gz
Source0  : http://urlgrabber.baseurl.org/download/urlgrabber-3.10.2.tar.gz
Summary  : A high-level cross-protocol url-grabber
Group    : Development/Tools
License  : LGPL-2.1
Requires: urlgrabber-bin
Requires: urlgrabber-license
Requires: urlgrabber-python
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
urlgrabber -- A high-level cross-protocol url-grabber
INSTALLATION INSTRUCTIONS
If you want to install urlgrabber on your system, simply open the package
and run:

%package bin
Summary: bin components for the urlgrabber package.
Group: Binaries
Requires: urlgrabber-license

%description bin
bin components for the urlgrabber package.


%package doc
Summary: doc components for the urlgrabber package.
Group: Documentation

%description doc
doc components for the urlgrabber package.


%package legacypython
Summary: legacypython components for the urlgrabber package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the urlgrabber package.


%package license
Summary: license components for the urlgrabber package.
Group: Default

%description license
license components for the urlgrabber package.


%package python
Summary: python components for the urlgrabber package.
Group: Default

%description python
python components for the urlgrabber package.


%prep
%setup -q -n urlgrabber-3.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528573198
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/urlgrabber
/usr/libexec/urlgrabber-ext-down

%files doc
%defattr(-,root,root,-)
/usr/share/doc/urlgrabber-3.10.2/ChangeLog
/usr/share/doc/urlgrabber-3.10.2/README
/usr/share/doc/urlgrabber-3.10.2/TODO

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/urlgrabber-3.10.2/LICENSE

%files python
%defattr(-,root,root,-)
