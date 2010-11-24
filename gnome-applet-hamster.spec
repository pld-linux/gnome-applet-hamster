%define		module	hamster-applet
Summary:	Project Hamster is time tracking for masses
Name:		gnome-applet-hamster
Version:	2.30.2
Release:	5
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hamster-applet/2.30/%{module}-%{version}.tar.bz2
# Source0-md5:	ad662fd81a09c5a0e19d1aa733e78588
Patch0:		%{name}-imports.diff
URL:		http://live.gnome.org/ProjectHamster
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-control-center-devel >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4.0
BuildRequires:	python-gnome-desktop-devel >= 2.22.0
BuildRequires:	python-modules-sqlite
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gnome-control-center >= 2.24.0
Requires:	python-gnome-desktop-applet >= 2.22.0
Requires:	python-gnome-desktop-libwnck >= 2.22.0
Requires:	python-gnome-gconf >= 2.22.0
Requires:	python-gnome-ui >= 2.22.0
Requires:	python-modules-sqlite
Requires:	rarian
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Project Hamster is time tracking for masses. It helps you to keep
track on how much time you have spent during the day on activities you
have set up.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-sqlite-detection
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitedir}/hamster/keybinder/*.la

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang hamster-applet --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install hamster-applet.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall hamster-applet.schemas

%postun
%update_icon_cache hicolor

%files -f hamster-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-time-tracker
%attr(755,root,root) %{_bindir}/hamster-standalone
%{_desktopdir}/hamster-standalone.desktop
%{_sysconfdir}/gconf/schemas/hamster-applet.schemas
%{_libdir}/bonobo/servers/*.server
%dir %{_libexecdir}/hamster-applet
%attr(755,root,root) %{_libexecdir}/hamster-applet/hamster-applet
%{_datadir}/hamster-applet
%{_datadir}/gnome-control-center/keybindings/99-hamster-applet.xml
%{py_sitedir}/hamster
%{_iconsdir}/hicolor/*/apps/hamster-applet.png
%{_iconsdir}/hicolor/*/apps/hamster-applet.svg
