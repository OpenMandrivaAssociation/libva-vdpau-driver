%define oname	libva-vdpau-driver

Name:		vaapi-driver-vdpau
Summary:	VA-API driver for VDPAU interface
Group:		Video
Version:	0.7.4
Release:	4
License:	GPLv2+
URL:		http://www.freedesktop.org
Source0:	http://www.freedesktop.org/software/vaapi/releases/libva-vdpau-driver/libva-vdpau-driver-%{version}.tar.bz2
# fix build with recent mesa (not a technically correct fix):
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(vdpau)
Provides:	%{oname} = %{version}-%{release}
Provides:	vdpau-video = %{version}-%{release}

Patch0:		PFNGLMULTITEXCOORD2FPROC_vaapi-driver-vdpau.patch
Patch1:		mesa-drivers.patch
Patch2:		sigfpe-crash.patch
Patch3:		libva-vdpau-driver-0.7.4-drop-h264-api.patch
Patch4:		vdpau.patch

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -qn %{oname}-%{version}/
%apply_patches

%build
autoreconf -fiv
%configure2_5x
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/dri/*.la

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so
