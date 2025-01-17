#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0D28D4D2A0ACE884 (bensberg@telfort.nl)
#
Name     : nano
Version  : 4.3
Release  : 59
URL      : https://www.nano-editor.org/dist/v4/nano-4.3.tar.xz
Source0  : https://www.nano-editor.org/dist/v4/nano-4.3.tar.xz
Source99 : https://www.nano-editor.org/dist/v4/nano-4.3.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: nano-bin = %{version}-%{release}
Requires: nano-data = %{version}-%{release}
Requires: nano-license = %{version}-%{release}
Requires: nano-man = %{version}-%{release}
BuildRequires : glibc-locale
BuildRequires : groff
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : slang-dev
Patch1: 0001-Support-a-stateless-configuration-by-default.patch

%description
GNU nano is a small and friendly text editor.  It aims to emulate the
Pico text editor while also offering several enhancements.

%package bin
Summary: bin components for the nano package.
Group: Binaries
Requires: nano-data = %{version}-%{release}
Requires: nano-license = %{version}-%{release}

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
Requires: nano-man = %{version}-%{release}

%description doc
doc components for the nano package.


%package license
Summary: license components for the nano package.
Group: Default

%description license
license components for the nano package.


%package man
Summary: man components for the nano package.
Group: Default

%description man
man components for the nano package.


%prep
%setup -q -n nano-4.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560863137
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%reconfigure --disable-static --disable-browser \
--disable-extra \
--disable-help \
--disable-histories \
--disable-justify \
--disable-libmagic \
--disable-nls \
--enable-utf8
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1560863137
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nano
cp COPYING %{buildroot}/usr/share/package-licenses/nano/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/nano/COPYING.DOC
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
/usr/share/nano/asm.nanorc
/usr/share/nano/autoconf.nanorc
/usr/share/nano/awk.nanorc
/usr/share/nano/c.nanorc
/usr/share/nano/changelog.nanorc
/usr/share/nano/cmake.nanorc
/usr/share/nano/css.nanorc
/usr/share/nano/debian.nanorc
/usr/share/nano/default.nanorc
/usr/share/nano/elisp.nanorc
/usr/share/nano/fortran.nanorc
/usr/share/nano/gentoo.nanorc
/usr/share/nano/go.nanorc
/usr/share/nano/groff.nanorc
/usr/share/nano/guile.nanorc
/usr/share/nano/html.nanorc
/usr/share/nano/java.nanorc
/usr/share/nano/javascript.nanorc
/usr/share/nano/json.nanorc
/usr/share/nano/lua.nanorc
/usr/share/nano/makefile.nanorc
/usr/share/nano/man.nanorc
/usr/share/nano/mgp.nanorc
/usr/share/nano/mutt.nanorc
/usr/share/nano/nanohelp.nanorc
/usr/share/nano/nanorc.nanorc
/usr/share/nano/nftables.nanorc
/usr/share/nano/objc.nanorc
/usr/share/nano/ocaml.nanorc
/usr/share/nano/patch.nanorc
/usr/share/nano/perl.nanorc
/usr/share/nano/php.nanorc
/usr/share/nano/po.nanorc
/usr/share/nano/postgresql.nanorc
/usr/share/nano/pov.nanorc
/usr/share/nano/python.nanorc
/usr/share/nano/ruby.nanorc
/usr/share/nano/rust.nanorc
/usr/share/nano/sh.nanorc
/usr/share/nano/spec.nanorc
/usr/share/nano/tcl.nanorc
/usr/share/nano/tex.nanorc
/usr/share/nano/texinfo.nanorc
/usr/share/nano/xml.nanorc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/nano/*
%doc /usr/share/info/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nano/COPYING
/usr/share/package-licenses/nano/COPYING.DOC

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nano.1
/usr/share/man/man1/rnano.1
/usr/share/man/man5/nanorc.5
