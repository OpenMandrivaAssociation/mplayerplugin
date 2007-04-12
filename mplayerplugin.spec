%define _mozillapluginpath	%{_libdir}/mozilla/plugins
%define _mozillacomponentpath	%{_libdir}/mozilla/plugins

Summary: A browser plugin to allow playing embedded movies on web pages
Name:    mplayerplugin
Version: 3.35
Release: %mkrel 1
License: GPL
Group:   Networking/WWW
URL: http://mplayerplug-in.sourceforge.net
Source0: http://heanet.dl.sourceforge.net/sourceforge/mplayerplug-in/mplayerplug-in-%{version}.tar.bz2
Patch0: mplayerplugin-3.01-mime.patch
BuildRequires: XFree86-devel
%if %{mdkversion} > 1020
BuildRequires: mozilla-firefox-devel
%else
BuildRequires: mozilla-devel
%endif
BuildRequires: gtk+2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: mplayer >= 0.92
Conflicts: mozplugger < 1.5.2-2mdk

%description
Mplayerplug-in is a Netscape/Mozilla browser plugin to allow
playing embedded movies on web pages.

%prep
%setup -n mplayerplug-in
%patch0 -p1 -b .mime

%build
%if %{mdkversion} > 1020
perl -pi -e 's/mozilla-/mozilla-firefox-/g' configure.in
aclocal
autoconf-2.5x
%endif

%configure2_5x \
	--enable-wmp \
	--enable-qt \
	--enable-gmp \
	--enable-rm \
	--enable-dvx \
	--enable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir} \
	$RPM_BUILD_ROOT%{_mozillapluginpath} \
	$RPM_BUILD_ROOT%{_mozillacomponentpath}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/mplayerplug-in.conf <<EOF
# Enable debugging if set to 1 (default=0)
debug=1

# Video output
vo=x11

# Audio output
ao=esd,alsa,oss,arts,null

# Passes display to show output to, useful for multiple monitor setups
#display=[display name]

# Tells mplayer to allow default video post processing or not (default=0)
#novop=1

# Pass special video post processing
#vopopt=[mplayer vop options]

# Option for rtsp streams, set to 1 when behind proxy (default=0)
rtsp-use-tcp=1

# OSD Level (default=0)
osdlevel=3

# When set to 1 uses the aspect of movie no matter what (default=1)
#prefer-aspect=0

# If set to 1, forces mplayer to be in it's own window (default=0)
#noembed=0

# If set to 1, mplayer will be launced in its own window if the url is not
# an embed tag (default=0)
#fileonly-embed=1

# Where to store the downloaded movies
dload-dir=\$HOME/tmp

# Download file before playing (default=0)
#download=1

# Set to 1 if you want to keep downloaded media (default=0)
#keep-download=1

# Cache Size in kB. This is the buffer size before the video plays (default=512)
cachesize=2048

# Percent of file to load into cache (default=25)
#cache-percent=10

# Read mime types to handle from \$HOME/{.mplayer,.mozilla}, /etc/mplayerplug-in.types
use-mimetypes=0

# Set QT Speeed, use "low" for dialup, "med" (default) for DSL, "high" for more
#qt-speed=low

# Enable/Disable Mpeg mime-types (default=1)
#enable-mpeg=0

# Enable/Disable MP3 Support (default=1)
#enable-mp3=0

# Enable/Disable Ogg mime-types (default=1)
#enable-ogg=0

# Enable/Disable Smil (default=1)
#enable-smil=0

# Enable/Disable Helix compatibility (not allowing nphelix.so to handle it's
# own mime types (default=1)
enable-helix=0

# Enable/Disable Windows Media Support (default=1)
#enable-wmp=0

# Enable/Disable QuickTime Support (default=1)
#enable-qt=0

# Enable/Disable RealMedia Support (default=1)
#enable-rm=0

# Enable PLS Support (default=1)
#enable-pls=0

# For Live.com video behind a proxy
#rtsp-use-tcp=0

# Black background
#black-background=0

# Disable media cache
#nomediacache=0

# Skip displaying some frames (default=0)
#framedrop=0

# Gradually adjusts the A/V sync based on audio delay measurements
#autosync=0

# Maximum A-V sync correction per frame
#mc=0

# User-Agent
#user-agent=NSPlayer

# Disable mouse button press/release input (default=1)
#nomouseinput=0

# Disable reading key events from standard input (default=1)
#noconsolecontrols=1

# Send cookies when making HTTP request
#cookies=1

# When set to 1 disables the pausing of video files when they are
# covered/hidden in the browser (default=0)
nopauseonhide=1

# When set to 0, media will not start until play is clicked (default=1)
#autostart=0

# Option showing the logo, 0 = no logo shown (default=1)
#slowlogo=0

# Option showing the time in the progress bar, 0 = no time shown (default=1)
showtime=0

# Option shown the media progress bar, 0 = not shown (default=1)
#showtracker=0

# When set to 1, no status messages are shown (default=0)
#hidestatus=1
EOF

install -m 755 mplayerplug-in.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 644 mplayerplug-in.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 755 mplayerplug-in-wmp.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 644 mplayerplug-in-wmp.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 755 mplayerplug-in-qt.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 755 mplayerplug-in-qt.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 755 mplayerplug-in-rm.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 755 mplayerplug-in-rm.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 755 mplayerplug-in-gmp.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 755 mplayerplug-in-gmp.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 755 mplayerplug-in-dvx.so $RPM_BUILD_ROOT%{_mozillapluginpath}
install -m 755 mplayerplug-in-dvx.xpt $RPM_BUILD_ROOT%{_mozillacomponentpath}

install -m 644 mplayerplug-in.types $RPM_BUILD_ROOT%{_sysconfdir}

# install translations
%makeinstall_std -C po DESTDIR=$RPM_BUILD_ROOT
%find_lang mplayerplug-in

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mplayerplug-in.lang
%defattr(-,root,root,-)
%doc ChangeLog INSTALL README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mplayerplug-in.conf
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mplayerplug-in.types
%{_mozillapluginpath}/mplayerplug-in.so
%{_mozillapluginpath}/mplayerplug-in-wmp.so
%{_mozillapluginpath}/mplayerplug-in-qt.so
%{_mozillapluginpath}/mplayerplug-in-rm.so
%{_mozillapluginpath}/mplayerplug-in-gmp.so
%{_mozillapluginpath}/mplayerplug-in-dvx.so
%{_mozillacomponentpath}/mplayerplug-in.xpt
%{_mozillacomponentpath}/mplayerplug-in-wmp.xpt
%{_mozillacomponentpath}/mplayerplug-in-qt.xpt
%{_mozillacomponentpath}/mplayerplug-in-rm.xpt
%{_mozillacomponentpath}/mplayerplug-in-gmp.xpt
%{_mozillacomponentpath}/mplayerplug-in-dvx.xpt


