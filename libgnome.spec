%define glib2_version 1.3.13
%define libbonobo_version 1.110.0
%define libxml2_version 2.4.12
%define libxslt_version 1.0.7
%define gconf2_version 1.1.6
%define gnome_vfs2_version 1.9.4.91
%define orbit2_version 2.3.103

Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	1.110.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnome/%{name}-%{version}.tar.bz2
URL:		ftp://www.gnome.org/
Requires:	glib2 >= %{glib2_version}
Requires:	libbonobo >= %{libbonobo_version}
Requires:	gnome-vfs2 >= %{gnome_vfs2_version}
Requires:	libxml2 >= %{libxml2_version}
Requires:	ORBit2 >= %{orbit2_version}
Requires:	libxslt >= %{libxslt_version}
## prereq for gconftool
PreReq:		GConf2 >= %{gconf2_version}
PreReq:		/sbin/ldconfig
BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	libbonobo-devel >= %{libbonobo_version}
BuildRequires:	GConf2-devel >= %{gconf2_version}
BuildRequires:	gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires:	libxml2-devel >= %{libxml2_version}
BuildRequires:	ORBit2-devel >= %{orbit2_version}
BuildRequires:	libxslt-devel >= %{libxslt_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Added to avoid the warning messages about utmp group, bug #24171
# fixme, just libzvt?
PreReq:		utempter

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%description -l pl
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
uøytkownika zbiorem aplikacji i narzÍdzi do uøywania w po≥±czeniu z
menadøerem okien pod X Window System. Pakiet libgnome zawiera
biblioteki nie zwi±zane z graficznym interfejsem potrzebne do
uruchomienia GNOME. Pakiet libgnomeui zawiera biblioteki GNOME zaleøne
od X11.

%package devel
Summary:	Headers for libgnome
Summary(pl):	Pliki nag≥Ûwkowe libgnome
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Conflicts:	gnome-libs-devel < 1.4.1.2
Requires:	zlib-devel
Requires:	esound-devel
Requires:	ORBit2-devel >= %{orbit2_version}
Requires:	glib2-devel >= %{glib2_version}
Requires:	libbonobo-devel >= %{libbonobo_version}
Requires:	GConf2-devel >= %{gconf2_version}
Requires:	gnome-vfs2-devel >= %{gnome_vfs2_version}
Requires:	libxml2-devel >= %{libxml2_version}
Requires:	libxslt-devel >= %{libxslt_version}

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
Pliki nag≥Ûwkowe potrzebne do kompilowania programÛw korzystaj±cych
z libgnome.

%package static
Summary:	Static libgnome libraries
Summary(pl):	Statyczne biblioteki libgnome
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libgnome libraries.

%description static -l pl
Statyczna wersja bibliotek libgnome.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
export GCONF_CONFIG_SOURCE
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/desktop_gnome_*.schemas > /dev/null

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_libdir}/gnome-vfs-2.0/modules/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sgml
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/gnome-vfs-2.0/modules/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
