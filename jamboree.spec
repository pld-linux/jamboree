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
URL:		http://www.imendio.com/projects/jamboree/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel >= 1.8.0
BuildRequires:	gstreamer-GConf-devel >= 0.8.2
BuildRequires:	gstreamer-devel >= 0.8.2
BuildRequires:	gstreamer-plugins-devel >= 0.8.2
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libid3tag-devel >= 0.12
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
Requires(post):	GConf2
Requires:	gstreamer-audio-effects >= 0.8.2
Requires:	gstreamer-audiosink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jamboree is a music player.

%description -l pl
Jamboree to odtwarzacz muzyki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


mv po/{no,nb}.po

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--enable-dbus=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
echo "Remember to install appropriate gstreamer plugins for files"
echo "you want to play:"
echo "- gstreamer-mad (for MP3s)"
echo "- gstreamer-vorbis (for Ogg Vorbis)"

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*
%{_pixmapsdir}/*
