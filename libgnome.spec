%define glib2_version 1.3.13
%define libbonobo_version 1.110.0
%define libxml2_version 2.4.12
%define libxslt_version 1.0.7
%define gconf2_version 1.1.6
%define gnome_vfs2_version 1.9.4.91
%define orbit2_version 2.3.103

Summary: GNOME base library
Name: libgnome
Version: 1.110.0
Release: 1
URL: ftp://ftp.gnome.org
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root

Requires:  glib2 >= %{glib2_version}
Requires:  libbonobo >= %{libbonobo_version}
Requires:  gnome-vfs2 >= %{gnome_vfs2_version}
Requires:  libxml2 >= %{libxml2_version}
Requires:  ORBit2 >= %{orbit2_version}
Requires:  libxslt >= %{libxslt_version}
## prereq for gconftool
PreReq:  GConf2 >= %{gconf2_version}

BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:  libbonobo-devel >= %{libbonobo_version}
BuildRequires:  GConf2-devel >= %{gconf2_version}
BuildRequires:  gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires:  libxml2-devel >= %{libxml2_version}
BuildRequires:  ORBit2-devel >= %{orbit2_version}
BuildRequires:  libxslt-devel >= %{libxslt_version}


# Added to avoid the warning messages about utmp group, bug #24171
# fixme, just libzvt?
PreReq:                utempter

%description

GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.


%package devel
Summary: Libraries and headers for libgnome
Group: Development/Libraries
Requires:	%name = %{version}

Conflicts: gnome-libs-devel < 1.4.1.2
Requires:  zlib-devel
Requires:  esound-devel
Requires:  ORBit2-devel >= %{orbit2_version}
Requires:  glib2-devel >= %{glib2_version}
Requires:  libbonobo-devel >= %{libbonobo_version}
Requires:  GConf2-devel >= %{gconf2_version}
Requires:  gnome-vfs2-devel >= %{gnome_vfs2_version}
Requires:  libxml2-devel >= %{libxml2_version}
Requires:  libxslt-devel >= %{libxslt_version}

%description devel

GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome-devel package
includes the libraries and include files that you will need to
use libgnome.

You should install the libgnome-devel package if you would like to
compile GNOME applications. You do not need to install libgnome-devel
if you just want to use the GNOME desktop environment.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/desktop_gnome_*.schemas > /dev/null

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*
%{_libdir}/gnome-vfs-2.0/modules/*
%{_bindir}/*
%{_datadir}/sgml
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/gnome-vfs-2.0/modules/*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0

* Tue Jan 22 2002 Havoc Pennington <hp@redhat.com>
- remove bogus dependency on libdb1

* Thu Jan  3 2002 Havoc Pennington <hp@redhat.com>
- fix the post script

* Thu Jan  3 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 cvs snap

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- fix .schemas in post

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- update CVS snap to 1.107.0.90, glib 1.3.11
- add libxslt dep
- require specific versions of dependent libs
- add bunch of missing stuff to file list
- install gconf schemas in post

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- well, you only get the new CVS snap if you actually change the version in the spec file, doh

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, rebuild for glib 1.3.10, remove gtk requires

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new CVS snap, rebuild in 7.2-gnome

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
- remove gtk2 dependency, doh
