Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.9.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnome/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	dc071ed63171ae68c5833d1b55162642
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.9.2
BuildRequires:	audiofile-devel >= 1:0.2.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	esound-devel >= 1:0.2.31
BuildRequires:	gnome-vfs2-devel >= 2.9.90
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libbonobo-devel >= 2.6.2
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2 >= 2.9.2
Requires:	gnome-vfs2 >= 2.9.90
Obsoletes:	gnome-objc
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
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.9.2
Requires:	audiofile-devel >= 1:0.2.3
Requires:	esound-devel >= 1:0.2.31
Requires:	gnome-vfs2-devel >= 2.9.90
Requires:	gtk-doc-common

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnome libraries.

%description static -l pl
Statyczna wersja bibliotek libgnome.

%prep
%setup -q

%build
export _POSIX2_VERSION=199209 
glib-gettextize --force
intltoolize --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
export _POSIX2_VERSION=199209 
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

# no static modules and *.la for bonobo modules
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
