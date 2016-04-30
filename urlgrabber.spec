#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urlgrabber
Version  : 3.10.1
Release  : 12
URL      : http://urlgrabber.baseurl.org/download/urlgrabber-3.10.1.tar.gz
Source0  : http://urlgrabber.baseurl.org/download/urlgrabber-3.10.1.tar.gz
Summary  : A high-level cross-protocol url-grabber
Group    : Development/Tools
License  : LGPL-2.1
Requires: urlgrabber-bin
Requires: urlgrabber-python
Requires: urlgrabber-data
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : pycurl
BuildRequires : python-dev
BuildRequires : setuptools

%description
urlgrabber -- A high-level cross-protocol url-grabber
INSTALLATION INSTRUCTIONS
If you want to install urlgrabber on your system, simply open the package
and run:

%package bin
Summary: bin components for the urlgrabber package.
Group: Binaries
Requires: urlgrabber-data

%description bin
bin components for the urlgrabber package.


%package data
Summary: data components for the urlgrabber package.
Group: Data

%description data
data components for the urlgrabber package.


%package python
Summary: python components for the urlgrabber package.
Group: Default

%description python
python components for the urlgrabber package.


%prep
%setup -q -n urlgrabber-3.10.1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/urlgrabber
/usr/libexec/urlgrabber-ext-down

%files data
%defattr(-,root,root,-)
/usr/share/doc/urlgrabber-3.10.1/ChangeLog
/usr/share/doc/urlgrabber-3.10.1/LICENSE
/usr/share/doc/urlgrabber-3.10.1/README
/usr/share/doc/urlgrabber-3.10.1/TODO

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
