Summary:	Project Hamster is time tracking for masses
Name:		gnome-applet-hamster
Version:	0.6.1
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://projecthamster.googlecode.com/files/hamster-applet-%{version}.tar.gz
# Source0-md5:	c9aa0690c9dc8fda4a47cb8bb9434b3a
Patch0:		%{name}-pythondir.patch
URL:		http://projecthamster.wordpress.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-gnome-desktop-devel >= 2.22.0
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	python-sqlite >= 2.3.0
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
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
%setup -q -n hamster-applet-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/hamster-applet/*.la
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
%attr(755,root,root) %{_libdir}/hamster-applet/idle.so
%{_datadir}/hamster-applet
%{py_sitedir}/hamster
%{_iconsdir}/hicolor/*/apps/hamster-applet.png
%{_iconsdir}/hicolor/*/apps/hamster-applet.svg
