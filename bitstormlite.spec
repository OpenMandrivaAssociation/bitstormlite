%define name_orig	BitStormLite
%define	name	%(echo %{name_orig}|tr "A-Z" "a-z")

%define version 0.2k
%define release %mkrel 1

Summary:	A BitTorrent downloader GTK
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
URL:		http://bit-storm.spaces.live.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://prdownloads.sourceforge.net/bbom/%{name_orig}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	gtk2-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	boost-devel

%description
BitStormLite is a BitTorrent program use GTK2. It's main features are :
* Downloads torrent files 
* Upload speed capping, seeing that most people can't upload infinite
  amounts of data.

%prep
%setup -q -n %{name_orig}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%{find_lang} %{name_orig}

mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name_orig}
Comment=A BitTorrent downloader GTK
Exec=%{_bindir}/%{name}
Icon=file_transfer_section
Terminal=false
Type=Application
MimeType=application/x-bittorrent;
Categories=GTK;Network;FileTransfer;P2P;
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

%files -f %{name_orig}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
