Summary:	Music Player
Summary(pl):	Odtwarzacz muzyki
Name:		jamboree
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.gnome.org/~jdahlin/jamboree/%{name}-%{version}.tar.gz
# Source0-md5:	894b8805113c400c873cd112c36af9cc
Patch0:		%{name}-test-build.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel >= 1.8.0
BuildRequires:	gstreamer-devel >= 0.6.2
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libid3tag-devel >= 0.12
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
Requires(post):	scrollkeeper
Requires(post):	GConf2
Requires:	gstreamer-audiosink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jamboree is a music player.

%description -l pl
Jamboree to odtwarzacz muzyki.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/jamboree.schemas
%{_desktopdir}/*
%{_pixmapsdir}/jamboree.png
