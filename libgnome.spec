Summary:	GNOME base library
Summary(pl):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.12.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnome/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	0b5dc2ee288035bcbcfb3275216e7a9d
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	audiofile-devel >= 1:0.2.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	esound-devel >= 1:0.2.35
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.12.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.34.1
BuildRequires:	libbonobo-devel >= 2.10.1
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post):	/sbin/ldconfig
Requires(post,preun):	GConf2 >= 2.12.0
Requires:	gnome-vfs2 >= 2.12.0
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
Requires:	GConf2-devel >= 2.12.0
Requires:	audiofile-devel >= 1:0.2.3
Requires:	esound-devel >= 1:0.2.35
Requires:	gnome-vfs2-devel >= 2.12.0
Requires:	gtk-doc-common
Requires:	popt-devel >= 1.5

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
%{__glib_gettextize}
%{__intltoolize}
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
%gconf_schema_install desktop_gnome_accessibility_keyboard.schemas
%gconf_schema_install desktop_gnome_accessibility_startup.schemas
%gconf_schema_install desktop_gnome_applications_browser.schemas
%gconf_schema_install desktop_gnome_applications_help_viewer.schemas
%gconf_schema_install desktop_gnome_applications_terminal.schemas
%gconf_schema_install desktop_gnome_applications_window_manager.schemas
%gconf_schema_install desktop_gnome_background.schemas
%gconf_schema_install desktop_gnome_file_views.schemas
%gconf_schema_install desktop_gnome_interface.schemas
%gconf_schema_install desktop_gnome_lockdown.schemas
%gconf_schema_install desktop_gnome_peripherals_keyboard.schemas
%gconf_schema_install desktop_gnome_peripherals_mouse.schemas
%gconf_schema_install desktop_gnome_sound.schemas
%gconf_schema_install desktop_gnome_thumbnailers.schemas
%gconf_schema_install desktop_gnome_typing_break.schemas

%preun
%gconf_schema_uninstall desktop_gnome_accessibility_keyboard.schemas
%gconf_schema_uninstall desktop_gnome_accessibility_startup.schemas
%gconf_schema_uninstall desktop_gnome_applications_browser.schemas
%gconf_schema_uninstall desktop_gnome_applications_help_viewer.schemas
%gconf_schema_uninstall desktop_gnome_applications_terminal.schemas
%gconf_schema_uninstall desktop_gnome_applications_window_manager.schemas
%gconf_schema_uninstall desktop_gnome_background.schemas
%gconf_schema_uninstall desktop_gnome_file_views.schemas
%gconf_schema_uninstall desktop_gnome_interface.schemas
%gconf_schema_uninstall desktop_gnome_lockdown.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_keyboard.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_mouse.schemas
%gconf_schema_uninstall desktop_gnome_sound.schemas
%gconf_schema_uninstall desktop_gnome_thumbnailers.schemas
%gconf_schema_uninstall desktop_gnome_typing_break.schemas

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-open
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.so
%{_libdir}/bonobo/servers/*
%{_mandir}/man7/gnome-options*
%{_sysconfdir}/gconf/schemas/desktop_gnome_accessibility_keyboard.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_accessibility_startup.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_browser.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_help_viewer.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_terminal.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_window_manager.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_background.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_file_views.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_interface.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_lockdown.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_mouse.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_sound.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_thumbnailers.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_typing_break.schemas
%{_sysconfdir}/sound

%files devel
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%{_includedir}/libgnome-2.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
