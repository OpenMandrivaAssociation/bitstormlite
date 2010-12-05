%define name_orig	BitStormLite
%define	name	%(echo %{name_orig}|tr "A-Z" "a-z")

%define version 0.2p
%define release %mkrel 5

Summary:	A BitTorrent downloader GTK
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://sourceforge.net/projects/bbom/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://prdownloads.sourceforge.net/bbom/%{name_orig}-%{version}.tar.gz
Patch0:		BitStormLite-0.2m-desktop-file.patch
Patch1:		bitstormlite-0.2p-gcc43.patch
Patch2:		bitstormlite-0.2p-gcc44.patch
Patch3:		bitstormlite-0.2p-str-fmt.patch
Patch4:		bitstormlite-0.2p-link.patch
BuildRequires:	curl-devel
BuildRequires:	gtk2-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel

%description
BitStormLite is a BitTorrent program use GTK2. It's main features are :
* Downloads torrent files 
* Upload speed capping, seeing that most people can't upload infinite
  amounts of data.

%prep
%setup -q -n %{name_orig}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0 -b .link

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name_orig}

install -m644 -D %{name}.desktop %buildroot%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%files -f %{name_orig}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
