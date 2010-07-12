
%define name	vaapi-driver-vdpau
%define oname	vdpau-video
%define version	0.6.10
%define rel	1

Summary:	VA-API driver for VDPAU interface
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/
Source:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/%{oname}-%{version}.tar.gz
BuildRequires:	libva-devel
BuildRequires:	vdpau-devel

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/va/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_libdir}/va/drivers/*_drv_video.so