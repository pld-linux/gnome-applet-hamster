%define		module	hamster-applet
Summary:	Project Hamster is time tracking for masses
Name:		gnome-applet-hamster
Version:	2.24.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hamster-applet/2.24/%{module}-%{version}.tar.bz2
# Source0-md5:	fd05dbe0e010a2fcc35ab49e6dadcce7
URL:		http://live.gnome.org/ProjectHamster
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-control-center-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-gnome-desktop-devel >= 2.22.0
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	python-sqlite >= 2.3.0
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gnome-control-center
Requires:	python-gnome-desktop-applet >= 2.22.0
Requires:	python-gnome-gconf >= 2.22.0
Requires:	python-gnome-ui >= 2.22.0
Requires:	python-sqlite >= 2.3.0
Requires:	rarian
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Project Hamster is time tracking for masses. It helps you to keep
track on how much time you have spent during the day on activities you
have set up.

%prep
%setup -q -n %{module}-%{version}

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
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
%{_sysconfdir}/gconf/schemas/hamster-applet.schemas
%{_libdir}/bonobo/servers/*.server
%dir %{_libexecdir}/hamster-applet
%attr(755,root,root) %{_libexecdir}/hamster-applet/hamster-applet
%{_datadir}/hamster-applet
%{_datadir}/gnome-control-center/keybindings/99-hamster-applet.xml
%{py_sitedir}/hamster
%{_iconsdir}/hicolor/*/apps/hamster-applet.png
%{_iconsdir}/hicolor/*/apps/hamster-applet.svg
