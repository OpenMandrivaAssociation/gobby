Name:           gobby
Version:        0.4.5
Release:        %mkrel 1
Summary:        A free collaborative editor
Group:          Editors
License:        GPL
URL:            http://gobby.0x539.de/
Source0:        http://releases.0x539.de/%{name}/%{name}-%{version}.tar.bz2 
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  libnet6-devel libobby-devel gtkmm2.4-devel
BuildRequires:  gtksourceview-devel libxml++-devel
BuildRequires:  pkgconfig(gtksourceview-1.0)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  ImageMagick 
%description
Gobby is a free collaborative editor based on libobby, a library which provides
synced document buffers. It supports multiple documents in one session and a 
multi-user chat. It runs on Microsoft Windows, Mac OS X, Linux and other 
Unix-like platforms.

It uses GTK+ 2.6 as its windowing toolkit and thus integrates nicely into the 
GNOME desktop environment.

%prep
%setup -q
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gobby
Comment=A free collaborative editor
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Editors;TextEditor;
EOF


mkdir -p $RPM_BUILD_ROOT/%_iconsdir 
mkdir -p $RPM_BUILD_ROOT/%_liconsdir 
mkdir -p $RPM_BUILD_ROOT/%_miconsdir 

convert contrib/artwork/%{name}.svg -geometry 48x48 $RPM_BUILD_ROOT%_liconsdir/%{name}.png
convert contrib/artwork/%{name}.svg -geometry 32x32 $RPM_BUILD_ROOT%_iconsdir/%{name}.png
convert contrib/artwork/%{name}.svg -geometry 16x16 $RPM_BUILD_ROOT%_miconsdir/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README NEWS
%_bindir/*
%_liconsdir/%{name}.png
%_iconsdir/%{name}.png
%_miconsdir/%{name}.png
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%post
%{update_menus}

%postun
%{clean_menus}

