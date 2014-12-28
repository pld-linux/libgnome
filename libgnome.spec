#
# Conditional build:
%bcond_with	esd		# EsounD support (obsolete)
%bcond_without	static_libs	# static library

Summary:	GNOME base library
Summary(pl.UTF-8):	Podstawowa biblioteka GNOME
Name:		libgnome
Version:	2.32.1
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnome/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	a4345e6087ae6195d65a4674ffdca559
Patch0:		%{name}-load-config.patch
Patch1:		%{name}-glib.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
%{?with_esd:BuildRequires:	audiofile-devel >= 0.2.3}
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
%{?with_esd:BuildRequires:	esound-devel >= 0.2.26}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.24.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	libcanberra-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libbonobo >= 2.24.0
Suggests:	gnome-vfs2
Obsoletes:	gnome-objc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
użytkownika zbiorem aplikacji i narzędzi do używania w połączeniu z
zarządcą okien pod X Window System. Pakiet libgnome zawiera biblioteki
nie związane z graficznym interfejsem potrzebne do uruchomienia GNOME.
Pakiet libgnomeui zawiera biblioteki GNOME zależne od X11.

%package libs
Summary:	Base libgnome library and bonobo modules
Summary(pl.UTF-8):	Podstawowa biblioteka libgnome oraz moduły bonobo
Group:		Libraries
Requires:	GConf2-libs >= 2.24.0
Requires:	gnome-vfs2-libs >= 2.24.0
Requires:	libbonobo-libs >= 2.24.0
Requires:	popt >= 1.5
Conflicts:	libgnome < 2.32.0-3

%description libs
Base libgnome library and bonobo modules.

%description libs -l pl.UTF-8
Podstawowa biblioteka libgnome oraz moduły bonobo.

%package devel
Summary:	Headers for libgnome
Summary(pl.UTF-8):	Pliki nagłówkowe libgnome
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	gnome-vfs2-devel >= 2.24.0
Requires:	libbonobo-devel >= 2.24.0
Requires:	libcanberra-devel
Requires:	popt-devel >= 1.5

%description devel
This package includes the header files for libgnome applications
development.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów korzystających z
libgnome.

%package static
Summary:	Static libgnome libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnome libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libgnome.

%package apidocs
Summary:	libgnome API documentation
Summary(pl.UTF-8):	Dokumentacja API libgnome
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libgnome API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnome.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_esd:--enable-esd} \
	--enable-gtk-doc \
	--disable-schemas-install \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules and *.la for bonobo modules
# libraries .la obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.a
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install desktop_gnome_accessibility_keyboard.schemas
%gconf_schema_install desktop_gnome_accessibility_startup.schemas
%gconf_schema_install desktop_gnome_applications_at_mobility.schemas
%gconf_schema_install desktop_gnome_applications_at_visual.schemas
%gconf_schema_install desktop_gnome_applications_browser.schemas
%gconf_schema_install desktop_gnome_applications_office.schemas
%gconf_schema_install desktop_gnome_applications_terminal.schemas
%gconf_schema_install desktop_gnome_applications_window_manager.schemas
%gconf_schema_install desktop_gnome_background.schemas
%gconf_schema_install desktop_gnome_file_views.schemas
%gconf_schema_install desktop_gnome_interface.schemas
%gconf_schema_install desktop_gnome_lockdown.schemas
%gconf_schema_install desktop_gnome_peripherals_keyboard.schemas
%gconf_schema_install desktop_gnome_peripherals_mouse.schemas
%gconf_schema_install desktop_gnome_sound.schemas
%gconf_schema_install desktop_gnome_thumbnail_cache.schemas
%gconf_schema_install desktop_gnome_thumbnailers.schemas
%gconf_schema_install desktop_gnome_typing_break.schemas

%preun
%gconf_schema_uninstall desktop_gnome_accessibility_keyboard.schemas
%gconf_schema_uninstall desktop_gnome_accessibility_startup.schemas
%gconf_schema_uninstall desktop_gnome_applications_at_mobility.schemas
%gconf_schema_uninstall desktop_gnome_applications_at_visual.schemas
%gconf_schema_uninstall desktop_gnome_applications_browser.schemas
%gconf_schema_uninstall desktop_gnome_applications_office.schemas
%gconf_schema_uninstall desktop_gnome_applications_terminal.schemas
%gconf_schema_uninstall desktop_gnome_applications_window_manager.schemas
%gconf_schema_uninstall desktop_gnome_background.schemas
%gconf_schema_uninstall desktop_gnome_file_views.schemas
%gconf_schema_uninstall desktop_gnome_interface.schemas
%gconf_schema_uninstall desktop_gnome_lockdown.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_keyboard.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_mouse.schemas
%gconf_schema_uninstall desktop_gnome_sound.schemas
%gconf_schema_uninstall desktop_gnome_thumbnail_cache.schemas
%gconf_schema_uninstall desktop_gnome_thumbnailers.schemas
%gconf_schema_uninstall desktop_gnome_typing_break.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/gnome-open
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/gnome-default.xml
%dir %{_pixmapsdir}/backgrounds
%dir %{_pixmapsdir}/backgrounds/gnome
%{_pixmapsdir}/backgrounds/gnome/background-default.jpg
%{_mandir}/man7/gnome-options*
%{_sysconfdir}/gconf/schemas/desktop_gnome_accessibility_keyboard.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_accessibility_startup.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_at_mobility.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_at_visual.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_browser.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_office.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_terminal.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_applications_window_manager.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_background.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_file_views.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_interface.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_lockdown.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_mouse.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_sound.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_thumbnail_cache.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_thumbnailers.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_typing_break.schemas
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%{_sysconfdir}/sound/events/gtk-events-2.soundlist
%{_sysconfdir}/sound/events/gnome-2.soundlist

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-2.so.0
%attr(755,root,root) %{_libdir}/bonobo/monikers/libmoniker_extra_2.so
%{_libdir}/bonobo/servers/GNOME_Moniker_std.server

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-2.so
%{_includedir}/libgnome-2.0
%{_pkgconfigdir}/libgnome-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
