Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.4.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	caec1e12d64b98a2925a4317ac16429f
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.31
BuildRequires:	gnome-vfs2-devel >= 2.3.7
BuildRequires:	gtk-doc
BuildRequires:	libbonobo-devel >= 2.3.6
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	libxslt-devel >= 1.0.32
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	intltool >= 0.27.2
Requires(post):	GConf2 >= 2.3.3
Requires(post):	/sbin/ldconfig
Requires:	gnome-vfs2 >= 2.3.7
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
Requires:	GConf2-devel >= 2.3.3
Requires:	audiofile-devel >= 0.2.3
Requires:	esound-devel >= 0.2.31
Requires:	gnome-vfs2-devel >= 2.3.7
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 2.5.10

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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

# no static modules
rm -f $RPM_BUILD_ROOT%{_libdir}/{gnome-vfs-2.0/modules,bonobo/monikers}/*.a

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
%{_sysconfdir}/sound
%attr(755,root,root) %{_bindir}/gnome-open
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.so
%{_libdir}/bonobo/monikers/*.la
%{_libdir}/bonobo/servers/*

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
