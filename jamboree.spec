Name:		jamboree
Summary:	Music Player
Version:	0.3
Release:	1
License:	GPL
Source0:	http://www.gnome.org/~jdahlin/jamboree/%{name}-%{version}.tar.gz
# Source0-md5:	894b8805113c400c873cd112c36af9cc
Patch0:		%{name}-disable-test-build.patch
Group:		Applications/Multimedia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	gstreamer-devel >= 0.6.2
BuildRequires:	gstreamer-vorbis >= 0.6.2
BuildRequires:	gstreamer-mad >= 0.6.2
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	libid3tag-devel >= 0.12
BuildRequires:	gdbm-devel >= 1.8.0
Requires(post): scrollkeeper
Requires(post): GConf2
Requires:	gstreamer-audiosink
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jamboree is a music player

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-oggtest \
	--disable-vorbistest \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf %{buildroot}

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog FAQ INSTALL README NEWS
%{_sysconfdir}/gconf/schemas/jamboree.schemas
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*
%{_desktopdir}/*
%{_pixmapsdir}/jamboree.png
