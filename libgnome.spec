Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.1.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gnome-vfs2-devel >= 2.1.3-3
BuildRequires:	gtk-doc
BuildRequires:	libbonobo-devel >= 2.1.0-3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	libxslt-devel >= 1.0.20
BuildRequires:	openssl-devel
BuildRequires:	rpm-build >= 4.1-8.2
Requires:	gnome-vfs2 >= 2.0.4-3
Requires(post):	GConf2
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%description -l pl
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
u¿ytkownika zbiorem aplikacji i narzêdzi do u¿ywania w po³±czeniu z
zarz±dc± okien pod X Window System. Pakiet libgnome zawiera biblioteki
nie zwi±zane z graficznym interfejsem potrzebne do uruchomienia GNOME.
Pakiet libgnomeui zawiera biblioteki GNOME zale¿ne od X11.

%package devel
Summary:	Headers for libgnome
Summary(pl):	Pliki nag³ówkowe libgnome
Group:		Development/Libraries
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

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilowania programów korzystaj±cych z
libgnome.

%package static
Summary:	Static libgnome libraries
Summary(pl):	Statyczne biblioteki libgnome
Group:		Development/Libraries
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
%gconf_schema_install

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
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnome-2.0
%doc %{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-vfs-2.0/modules/*.a
%{_libdir}/bonobo/monikers/*.a
