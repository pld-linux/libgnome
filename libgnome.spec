Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.0.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.1/sources/libgnome/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		ftp://www.gnome.org/
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gtk-doc
BuildRequires:	gnome-vfs2-devel >= 2.0.3
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	libxslt-devel >= 1.0.20
BuildRequires:	openssl-devel
PreReq:		GConf2
PreReq:		/sbin/ldconfig
PreReq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%description -l pl
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
u¿ytkownika zbiorem aplikacji i narzêdzi do u¿ywania w po³±czeniu z
menad¿erem okien pod X Window System. Pakiet libgnome zawiera
biblioteki nie zwi±zane z graficznym interfejsem potrzebne do
uruchomienia GNOME. Pakiet libgnomeui zawiera biblioteki GNOME zale¿ne
od X11.

%package devel
Summary:	Headers for libgnome
Summary(pl):	Pliki nag³ówkowe libgnome
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	GConf2-devel >= 1.1.11
Requires:	audiofile-devel >= 0.2.3
Requires:	esound-devel >= 0.2.25
Requires:	gnome-vfs2-devel >= 1.9.17
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 2.4.20

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome-devel package
includes the libraries and include files that you will need to use
libgnome.

You should install the libgnome-devel package if you would like to
compile GNOME applications. You do not need to install libgnome-devel
if you just want to use the GNOME desktop environment.

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilowania programów korzystaj±cych z
libgnome.

%package static
Summary:	Static libgnome libraries
Summary(pl):	Statyczne biblioteki libgnome
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libgnome libraries.

%description static -l pl
Statyczna wersja bibliotek libgnome.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	HTML_DIR=%{_gtkdocdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
GCONF_CONFIG_SOURCE="" gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/sound/events/*
%attr(755,root,root) %{_libdir}/gnome2-db2html
%attr(755,root,root) %{_libdir}/gnome2-info2html
%attr(755,root,root) %{_libdir}/gnome2-man2html
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.??
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.??
%{_libdir}/bonobo/servers/*
%{_datadir}/sgml/docbook/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnome-2.0
%doc %{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-vfs-2.0/modules/*.a
%{_libdir}/bonobo/monikers/*.a
