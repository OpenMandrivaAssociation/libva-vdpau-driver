
%define name	vaapi-driver-vdpau
%define oname	vdpau-video
%define version	0.7.2
%define rel	1

Summary:	VA-API driver for VDPAU interface
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/
Source:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/%{oname}-%{version}.tar.gz
# fix build with recent mesa (not a technically correct fix):
Patch0:		vdpau-video-mesa.patch
BuildRequires:	libva-devel
BuildRequires:	vdpau-devel
Provides:	%oname

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -q -n %oname-%version
%apply_patches

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
