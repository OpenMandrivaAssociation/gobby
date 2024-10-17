Name:           gobby
Version:        0.4.13
Release:        1 
Summary:        A free collaborative editor
Group:          Editors
License:        GPLv2+
URL:            https://gobby.0x539.de/
Source0:        http://releases.0x539.de/gobby/%{name}-%{version}.tar.gz
BuildRequires:	libobby-devel >= 0.4.6
BuildRequires:  libnet6-devel libobby-devel gtkmm2.4-devel
BuildRequires:  gtksourceview-devel libxml++-devel
BuildRequires:  pkgconfig(gtksourceview-1.0)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  imagemagick 
BuildRequires:	intltool

%description
Gobby is a free collaborative editor based on libobby, a library which provides
synced document buffers. It supports multiple documents in one session and a 
multi-user chat. It runs on Microsoft Windows, Mac OS X, Linux and other 
Unix-like platforms.

It uses GTK+ 2.6 as its windowing toolkit and thus integrates nicely into the 
GNOME desktop environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gobby
Comment=A free collaborative editor
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=TextEditor;Utility;GTK;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS README NEWS
%_bindir/*
%_iconsdir/*/*/*/*
%{_datadir}/gobby/icons/*/*
%{_datadir}/applications/*
%{_mandir}/man1/*
