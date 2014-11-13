Summary:	VA-API driver for VDPAU interface
Name:		libva-vdpau-driver
Group:		Video
Version:	0.7.4
Release:	9
License:	GPLv2+
URL:		http://www.freedesktop.org/wiki/Software/vaapi/
Source0:	http://www.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}.tar.bz2
# fix build with recent mesa (not a technically correct fix):
Patch0:		PFNGLMULTITEXCOORD2FPROC_vaapi-driver-vdpau.patch
Patch1:		libva-vdpau-driver-0.7.4-drop-h264-api.patch
# API changes: http://cgit.freedesktop.org/~aplattner/libvdpau/commit/?id=186195b1a84f2517205522e7ab8e0f62ad61c329
Patch2:		libva-vdpau-driver-0.7.4-libvdpau0.8.patch
BuildRequires:	pkgconfig(libva) >= 1.2.0
BuildRequires:	pkgconfig(vdpau)
Provides:	vdpau-video = %{version}-%{release}
%rename		vaapi-driver-vdpau

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -qn %{oname}-%{version}/
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/dri/*.la

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so