#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nano
Version  : 2.5.3
Release  : 27
URL      : http://www.nano-editor.org/dist/v2.5/nano-2.5.3.tar.gz
Source0  : http://www.nano-editor.org/dist/v2.5/nano-2.5.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: nano-bin
Requires: nano-data
Requires: nano-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : slang-dev
BuildRequires : texinfo
Patch1: stateless.patch

%description
GNU nano is a small and friendly text editor.  It aims to emulate the
Pico text editor while also offering several enhancements.

%package bin
Summary: bin components for the nano package.
Group: Binaries
Requires: nano-data

%description bin
bin components for the nano package.


%package data
Summary: data components for the nano package.
Group: Data

%description data
data components for the nano package.


%package doc
Summary: doc components for the nano package.
Group: Documentation

%description doc
doc components for the nano package.


%prep
%setup -q -n nano-2.5.3
%patch1 -p1

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%reconfigure --disable-static --disable-extra \
--disable-libmagic \
--enable-tiny \
--disable-glibtest \
--disable-nls \
--disable-color
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nano
/usr/bin/rnano

%files data
%defattr(-,root,root,-)
/usr/share/defaults/nano/nanorc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/nano/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
