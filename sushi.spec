Summary:	A quick previewer for Nautilus
Name:		sushi
Version:	3.6.1
Release:	1
License:	GPLv2+ with exceptions
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	452d3935c3276fe1c61eb5a6cd5df847
URL:		https://live.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	evince-devel
BuildRequires:	gjs-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-webkit-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun): glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/sushi

%description
Sushi is a quick previewer for Nautilus.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/sushi/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/sushi
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/sushi-start
%dir %{_libdir}/sushi
%dir %{_libdir}/sushi/girepository-1.0
%attr(755,root,root) %{_libdir}/sushi/libsushi-1.0.so
%{_libdir}/sushi/girepository-1.0/Sushi-1.0.typelib
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
%{_datadir}/glib-2.0/schemas/org.gnome.sushi.gschema.xml

