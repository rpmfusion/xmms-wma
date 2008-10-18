%define xmms_inputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Input)

Summary: X MultiMedia System input plugin to play Windows Media Audio files
Name: xmms-wma
Version: 1.0.5
Release: 5%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://mcmcc.bat.ru/xmms-wma/
Source: http://mcmcc.bat.ru/xmms-wma/xmms-wma-%{version}.tar.bz2
Patch: xmms-wma-1.0.5-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: xmms-devel, gtk+-devel

%description
X MultiMedia System input plugin to play Windows Media Audio, aka WMA files.
This plug-in is written using the ffmpeg library (http://ffmpeg.sf.net)
written by Fabrice Bellard (to be exact, strongly advanced library).
Everything besides wma format support was removed from it to make it lighter.
Tag informations are converted from unicode to your system locale.


%prep
%setup -q
%patch -p1 -b .build


%build
%{__make} %{?_smp_mflags} OPTFLAGS="%{optflags} -finline-functions"


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 libwma.so %{buildroot}%{xmms_inputdir}/libwma.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, -)
%lang(ru) %doc readme.rus
%doc COPYING readme.eng
%{xmms_inputdir}/libwma.so


%changelog
* Sat Oct 18 2008 Orcan Ogetbil <orcanbahri AT yahoo Dot com> 1.0.5-5
- Minor spec file improvements.
- License is GPLv2+.

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0.5-4
- rebuild for RPM Fusion

* Mon Apr 10 2006 Matthias Saou <http://freshrpms.net/> 1.0.5-3
- Remove explicit xmms requirement, since we really only require the libs.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.5-2
- Release bump to drop the disttag number in FC5 build.

* Fri Dec  2 2005 Matthias Saou <http://freshrpms.net/> 1.0.5-1
- Update to 1.0.5.
- Drop gcc4 patch, got fixed in 1.0.4.1.
- Update build patch, seems like -fPIC got added at least in one place, but I
  don't think it's sufficient.

* Wed Jun 15 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-4
- Force -finline-functions to work around possible bug in gcc 3.x (not 4.x),
  thanks to Wesley Wright again.

* Wed Jun  8 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-3
- Include build patch with changes from Wesley Wright.

* Sun Jun  5 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-2
- Disable explicit stripping to get useful debuginfo package.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.
- Added gcc4 compile fix (http://gcc.gnu.org/ml/gcc/2005-02/msg00053.html).

* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Initial rpm package.

