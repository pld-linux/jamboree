Summary:	Music Player
Summary(pl):	Odtwarzacz muzyki
Name:		jamboree
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	23a0b5e3eda5e73bf838af66ba4b3180
Patch0:		%{name}-gst_plugins.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-deprecations.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel >= 1.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.12
BuildRequires:	gstreamer08x-GConf-devel >= 0.8.12
BuildRequires:	gstreamer08x-devel >= 0.8.12
BuildRequires:	gtk+2-devel >= 2:2.3.6
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libid3tag-devel >= 0.12
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
Requires(post,preun):	GConf2
Requires:	gstreamer08x-audio-effects >= 0.8.0
Requires:	gstreamer-audiosink < 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jamboree is a music player.

%description -l pl
Jamboree to odtwarzacz muzyki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

mv po/{no,nb}.po

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--enable-dbus=no \
	--enable-xine=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install jamboree.schemas
%banner %{name} -e << EOF
Remember to install appropriate GStreamer plugins for files
you want to play:
- gstreamer08x-flac (for FLAC)
- gstreamer08x-mad (for MP3s)
- gstreamer08x-vorbis (for Ogg Vorbis)
EOF

%preun
%gconf_schema_uninstall rhythmbox.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/jamboree.schemas
%{_desktopdir}/*
%{_pixmapsdir}/jamboree.png
