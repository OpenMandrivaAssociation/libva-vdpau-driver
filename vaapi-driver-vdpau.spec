%define oname	vdpau-video

Name:		vaapi-driver-vdpau
Summary:	VA-API driver for VDPAU interface
Group:		Video
Version:	0.7.3
Release:2
License:	GPLv2+
URL:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/
Source0:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/%{oname}-%{version}.tar.gz
# fix build with recent mesa (not a technically correct fix):
BuildRequires:	libva-devel
BuildRequires:	vdpau-devel
Provides:	%{oname} = %{version}-%{release}

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -qn %oname-%version

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/va/drivers/*.la

%files
%doc AUTHORS NEWS
%{_libdir}/va/drivers/*_drv_video.so
