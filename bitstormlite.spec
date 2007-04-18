%define name_orig	BitStormLite
%define	name	%(echo %{name_orig}|tr "A-Z" "a-z")

%define version 0.2h
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
Patch0:		%{name}-0.2g-svn-r21.patch
BuildRequires:	curl-devel
BuildRequires:	gtk2-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	boost-devel
BuildRequires:	cvs, autoconf2.5

%description
BitStormLite is a BitTorrent program use GTK2. It's main features are :
* Downloads torrent files 
* Upload speed capping, seeing that most people can't upload infinite
  amounts of data.

%prep
%setup -q -n %{name_orig}-%{version}
#%patch0 -p1 -b .svn-r21

%build
#chmod +x ./autogen.sh
#./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%{find_lang} %{name_orig}

# Menu item
mkdir -p %buildroot%_menudir
cat > %buildroot%{_menudir}/%{name} << EOF
?package(%name): needs="x11" \
	section="Internet/File Transfer" \
	title="%{name_orig}" \
	longtitle="A BitTorrent downloader GTK" \
	command="%{_bindir}/%{name}" \
	mimetypes="application/x-bittorrent" \
	startup_notify="true" \
	accept_url="false" \
	icon="file_transfer_section.png" \
	multiple_files="false" \
	xdg="true"
EOF

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
Categories=GTK;X-MandrivaLinux-Internet-FileTransfer;Network;FileTransfer;P2P;
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus
%update_desktop_database

%postun
%update_menus
%clean_desktop_database

%files -f %{name_orig}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_menudir}/%{name}
