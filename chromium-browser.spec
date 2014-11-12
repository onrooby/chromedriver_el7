# Based on Tom Callaway's <spot@fedoraproject.org> work

# ${nil} for Stable; -beta for Beta; -dev for Devel
# dash in -beta and -dev is intentional !
%define chromium_channel %{nil}
%define chromium_browser_channel chromium-browser%{chromium_channel}
%define chromium_path /opt/chromium-browser%{chromium_channel}
%define flash_version 15.0.0.189
%define tests 0
%define debug 0
%define flash 0

##############                      ! WARNING !                     ##############
### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)  ###
### Note: These are for CentOS use ONLY.                                       ###
### For your own distribution, please get your own set of keys.                ###
### http://lists.debian.org/debian-legal/2013/11/msg00006.html                 ###
%define api_key AIzaSyBFNqVTy5TNqIg7_p8LT6J-rOvCrP-g2OQ 
%define default_client_id 425408526734.apps.googleusercontent.com 
%define default_client_secret lE75DTSrowAf4PCLJwDnZT9h 

Name:		chromium-browser%{chromium_channel}
Version:	38.0.2125.104
Release:	1%{?dist}
Summary:	A WebKit (Blink) powered web browser
Url:		http://www.chromium.org/Home
# PepperFlash is licensed under Google Chrome ToS
# https://www.google.com/intl/en/chrome/browser/privacy/eula_text.html
License:	BSD and LGPLv2+
Group:		Applications/Internet

Patch0:		libudev_extern_c.patch
Patch1:		chromium-38.0.2125.44-gcc_workaround_modules_geolocation.patch
Patch2:		chromium-38.0.2125.44-gcc_workaround_core_inspector.patch
Patch3:		chromium-38.0.2125.44-gcc_workaround_mojo_application_manager.patch
Patch4:		chromium-38.0.2125.44-no_c++11_net_base.patch
Patch5:		chromium-38.0.2125.44-gcc_pragma.patch
Patch6:		chromium-38.0.2125.44-gcc_workaround_core_dom.patch
Patch7:		chromium-31.0.1650.57-python_simplejson.patch
Patch8:		chromium-38.0.2125.44-size_max.patch
Patch9:		chromium-37.0.2062.20-python_tld_cleanup.patch
Patch10:	chromium-38.0.2125.44-gcc_workaround_webui_omnibox.patch
Patch11:	chromium-38.0.2125.44-gcc_workaround_platform_heap.patch
Patch12:	chromium-37.0.2062.20-g_list_free_full.patch
# https://code.google.com/p/trace-viewer/issues/detail?id=590
# https://code.google.com/p/trace-viewer/source/detail?r=1485#
Patch13:	chromium-38.0.2125.44-tvcm_fix.patch
# https://codereview.appspot.com/129440043/
Patch14:	chromium-38.0.2125.44-trace_viewer.patch
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=39509
Patch15:	chromium-36.0.1985.32-v8_sink.patch
Patch16:	chromium-38.0.2125.44-python_re_sub.patch
Patch17:	chromium-38.0.2125.44-gcc_workaround_angle.patch
# We can't do a functional pointer to macro..
Patch18:	chromium-34.0.1847.132-gnome_keyring_fix.patch
Patch19:	chromium-38.0.2125.44-python_dict_generators.patch
Patch20:	chromium-35.0.1916.114-gdk_compat.patch
Patch21:	chromium-36.0.1985.32-gcc_workaround_browser_local_discovery.patch
# We don't have python-argparse in RHEL6, so bundle it like in Firefox package
Patch22:	python-argparse.patch
Patch23:	chromium-38.0.2125.44-gcc_workaround_modules_filesystem.patch
Patch24:	chromium-38.0.2125.44-gcc_workaround_modules_indexeddb.patch
Patch25:	chromium-38.0.2125.44-no_c++11_modules_serviceworkers.patch
Patch26:	chromium-38.0.2125.44-gcc_workaround_modules_webdatabase.patch
Patch27:	chromium-38.0.2125.44-cmath_round.patch
Patch28:	chromium-38.0.2125.44-no_c++11_browser_gpu.patch
Patch29:	chromium-38.0.2125.44-no_c++11_browser_service_worker.patch
Patch30:	chromium-38.0.2125.44-no_c++11_renderer_mojo.patch
Patch31:	chromium-38.0.2125.44-no_c++11_events_x.patch
Patch32:	chromium-38.0.2125.44-no_c++11_extensions_permissions.patch
Patch33:	chromium-38.0.2125.44-no_c++11_wm_overview.patch
Patch34:	chromium-38.0.2125.44-gcc_workaround_extensions_browser.patch
Patch35:	chromium-38.0.2125.44-no_c++11_api_notification_provider.patch
Patch36:	chromium-38.0.2125.44-gcc_workaround_app_list_search.patch
Patch37:	chromium-38.0.2125.44-no_c++11_browser_search.patch
Patch38:	chromium-38.0.2125.44-gcc_workaround_browser_ssl.patch
Patch39:	chromium-38.0.2125.44-no_c++11_browser_ssl.patch
Patch40:	chromium-38.0.2125.44-gcc_workaround_guest_view_extension_options.patch
Patch41:	chromium-38.0.2125.44-no_c++11_browser_notifications.patch
Patch42:	chromium-38.0.2125.44-no_c++11_browser_media_galleries.patch
Patch43:	chromium-38.0.2125.44-gcc_workaround_crypto_poly1305.patch
Patch44:	chromium-38.0.2125.101-no_c++11_browser_profiles.patch

### Chromium Tests Patches ###
Patch100:	chromium-32.0.1700.68-gcc_workaround_base_strings.patch
Patch101:	chromium-38.0.2125.101-no_c++11_net_http.patch

### Chromium Debug Build Patches ###
Patch200:	chromium-34.0.1847.132-debug_no_rtti.patch

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium RHEL use chromium-latest.py --stable --rhel --tests
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
Source0:	chromium-%{version}-clean.tar.xz
Source1:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}-testdata.tar.xz
# https://chromium.googlesource.com/chromium/tools/depot_tools.git/+/d5a1ab12efbc1c790a9bf3da57a74bf37d7205bc
Source2:	depot_tools.git-master.tar.gz
Source3:	chromium-browser.sh
Source4:	%{chromium_browser_channel}.desktop
# Also, only used if you want to reproduce the clean tarball.
Source5:	clean_ffmpeg.sh
Source6:	chromium-latest.py
Source7:	process_ffmpeg_gyp.py
%if %{?flash}
# https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
Source8:	libpepflashplayer.so.x86_64
Source9:	manifest.json.x86_64
# https://dl.google.com/linux/direct/google-chrome-stable_current_i386.rpm
Source11:	libpepflashplayer.so.i386
Source12:	manifest.json.i386
%endif

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc-c++, bison, flex, gtk2-devel, atk-devel
BuildRequires:	nss-devel >= 3.12.3
BuildRequires:	pciutils-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	cups-devel
BuildRequires:	libudev-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	glibc-devel
BuildRequires:	libXtst-devel
BuildRequires:	fontconfig-devel, GConf2-devel, dbus-devel
BuildRequires:	glib2-devel
BuildRequires:	gperf
BuildRequires:	alsa-lib-devel
BuildRequires:	libusb-devel, expat-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libdrm-devel
BuildRequires:	libcap-devel
BuildRequires:	libexif-devel
# Tests needs X
%if %{?tests}
BuildRequires:	Xvfb
%endif

# GTK modules it expects to find for some reason.
Requires:	libcanberra-gtk2%{_isa}
# semanage
Requires:	policycoreutils-python

ExclusiveArch:	%{ix86} arm x86_64

%description
Chromium is an open-source web browser, powered by WebKit (Blink).

%prep
%setup -q -T -c -n depot_tools -a 2
%setup -q -n chromium-%{version} -b 1

%patch0 -p1 -b .libudev_extern_c
%patch1 -p1 -b .gcc_workaround_modules_geolocation
%patch2 -p1 -b .gcc_workaround_core_inspector
%patch3 -p1 -b .gcc_workaround_mojo_application_manager
%patch4 -p1 -b .no_c++11_net_base
%patch5 -p1 -b .gcc_pragma
%patch6 -p1 -b .gcc_workaround_core_dom
%patch7 -p1 -b .python_simplejson
%patch8 -p1 -b .size_max
%patch9 -p1 -b .python_tld_cleanup
%patch10 -p1 -b .gcc_workaround_webui_omnibox
%patch11 -p1 -b .gcc_workaround_platform_heap
%patch12 -p1 -b .g_list_free_full
%patch13 -p1 -b .tvcm_fix
%patch14 -p1 -b .trace_viewer
%patch15 -p1 -b .v8_sink
%patch16 -p1 -b .python_re_sub
%patch17 -p1 -b .gcc_workaround_angle
%patch18 -p1 -b .gnome_keyring_fix
%patch19 -p1 -b .python_dict_generators
%patch20 -p1 -b .gdk_compat
%patch21 -p1 -b .gcc_workaround_browser_local_discovery
%patch22 -p1 -b .python_argparse
%patch23 -p1 -b .gcc_workaround_modules_filesystem
%patch24 -p1 -b .gcc_workaround_modules_indexeddb
%patch25 -p1 -b .no_c++11_modules_serviceworkers
%patch26 -p1 -b .gcc_workaround_modules_webdatabase
%patch27 -p1 -b .cmath_round
%patch28 -p1 -b .no_c++11_browser_gpu
%patch29 -p1 -b .no_c++11_browser_service_worker
%patch30 -p1 -b .no_c++11_renderer_mojo
%patch31 -p1 -b .no_c++11_events_x
%patch32 -p1 -b .no_c++11_extensions_permissions
%patch33 -p1 -b .no_c++11_wm_overview
%patch34 -p1 -b .gcc_workaround_extensions_browser
%patch35 -p1 -b .no_c++11_api_notification_provider
%patch36 -p1 -b .gcc_workaround_app_list_search
%patch37 -p1 -b .no_c++11_browser_search
%patch38 -p1 -b .gcc_workaround_browser_ssl
%patch39 -p1 -b .no_c++11_browser_ssl
%patch40 -p1 -b .gcc_workaround_guest_view_extension_options
%patch41 -p1 -b .no_c++11_browser_notifications
%patch42 -p1 -b .no_c++11_browser_media_galleries
%patch43 -p1 -b .gcc_workaround_crypto_poly1305
%patch44 -p1 -b .no_c++11_browser_profiles

### Chromium Tests Patches ###
%patch100 -p1 -b .gcc_workaround_base_strings
%patch101 -p1 -b .no_c++11_net_http

### Chromium Debug Build Patches ###
%if %{?debug}
%patch200 -p1 -b .no_rtti
%endif

# Set PYTHON PATH to directory which contains python argparse module
export PYTHONPATH=`pwd`/third_party/python-argparse

# Update gyp files according to our configuration
# If you will change something in the configuration please update it
# for build/gyp_chromium as well (and vice versa).
# FIXME: There should be a way how to avoid this duplication.
build/linux/unbundle/replace_gyp_files.py \
%ifarch x86_64
	-Dtarget_arch=x64 \
	-Dsystem_libdir=lib64 \
%endif
	-Dgoogle_api_key="%{api_key}" \
	-Dgoogle_default_client_id="%{default_client_id}" \
	-Dgoogle_default_client_secret="%{default_client_secret}" \
	-Ddisable_glibc=1 \
	-Ddisable_nacl=1 \
	-Ddisable_sse2=1 \
	-Dlinux_link_gnome_keyring=1 \
	-Dlinux_link_gsettings=1 \
	-Dlinux_link_libpci=1 \
	-Dlinux_link_libgps=0 \
	-Dlinux_sandbox_path=%{chromium_path}/chrome-sandbox \
	-Dlinux_sandbox_chrome_path=%{chromium_path}/chromium-browser \
	-Dlinux_strip_binary=1 \
	-Dlinux_use_gold_binary=0 \
	-Dlinux_use_gold_flags=0 \
	-Dlinux_use_libgps=0 \
	-Dno_strict_aliasing=1 \
	-Dproprietary_codecs=0 \
	-Dremove_webcore_debug_symbols=1 \
	-Duse_gconf=0 \
	-Duse_gnome_keyring=1 \
	-Duse_pulseaudio=1 \
	-Dffmpeg_branding=Chromium \
	-Dlogging_like_official_build=1 \
	-Dv8_no_strict_aliasing=1 \
	-Duse_gio=0 \
	-Dclang=0 \
	-Dhost_clang=0 \
	-Dwerror=

# From 38.x the boringssl is used for tests, without the possibility of using
# the system openssl instead.
# Remove the openssl and boringssl sources when not building the tests.
%if !%{?tests}
find third_party/openssl/ '(' -type l -or -type f ')'  -not '(' -name '*.gyp' -or -name '*.gypi' ')' -delete
find third_party/boringssl/ '(' -type l -or -type f ')'  -not '(' -name '*.gyp' -or -name '*.gypi' ')' -delete
%endif

build/gyp_chromium \
	--depth . \
%ifarch x86_64
	-Dtarget_arch=x64 \
	-Dsystem_libdir=lib64 \
%endif
	-Dgoogle_api_key="%{api_key}" \
	-Dgoogle_default_client_id="%{default_client_id}" \
	-Dgoogle_default_client_secret="%{default_client_secret}" \
	-Ddisable_glibc=1 \
	-Ddisable_nacl=1 \
	-Ddisable_sse2=1 \
	-Dlinux_link_gnome_keyring=1 \
	-Dlinux_link_gsettings=1 \
	-Dlinux_link_libpci=1 \
	-Dlinux_link_libgps=0 \
	-Dlinux_sandbox_path=%{chromium_path}/chrome-sandbox \
	-Dlinux_sandbox_chrome_path=%{chromium_path}/chromium-browser \
	-Dlinux_strip_binary=1 \
	-Dlinux_use_gold_binary=0 \
	-Dlinux_use_gold_flags=0 \
	-Dlinux_use_libgps=0 \
	-Dno_strict_aliasing=1 \
	-Dproprietary_codecs=0 \
	-Dremove_webcore_debug_symbols=1 \
	-Duse_gconf=0 \
	-Duse_gnome_keyring=1 \
	-Duse_pulseaudio=1 \
	-Dffmpeg_branding=Chromium \
	-Dlogging_like_official_build=1 \
	-Dv8_no_strict_aliasing=1 \
	-Duse_gio=0 \
	-Dclang=0 \
	-Dhost_clang=0 \
	-Dwerror=
#	-Duse_allocator=0 \

%build

%if %{?tests}
%define tests_targets base_unittests cacheinvalidation_unittests content_unittests crypto_unittests net_unittests printing_unittests sql_unittests
#gpu_unittests
#media_unittests
%else
%define tests_targets %{nil}
%endif

%if %{?debug}
%define target out/Debug
%else
%define target out/Release
%endif

# Set PYTHON PATH to directory which contains python argparse module
export PYTHONPATH=`pwd`/third_party/python-argparse

../depot_tools/ninja -C %{target} -vvv chrome chrome_sandbox chromedriver %{tests_targets}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{chromium_path}
cp -a %{SOURCE3} %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
export BUILDTARGET=`cat /etc/redhat-release`
export CHROMIUM_PATH=%{chromium_path}
export FLASH_VERSION=%{flash_version}
export CHROMIUM_BROWSER_CHANNEL=%{chromium_browser_channel}
sed -i "s|@@BUILDTARGET@@|$BUILDTARGET|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
sed -i "s|@@CHROMIUM_PATH@@|$CHROMIUM_PATH|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
sed -i "s|@@FLASH_VERSION@@|$FLASH_VERSION|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
sed -i "s|@@CHROMIUM_BROWSER_CHANNEL@@|$CHROMIUM_BROWSER_CHANNEL|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%if %{?flash}
sed -i "s|@@FLASH_ENABLED@@|1|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%else
sed -i "s|@@FLASH_ENABLED@@|0|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%endif
ln -s %{chromium_path}/%{chromium_browser_channel}.sh %{buildroot}%{_bindir}/%{chromium_browser_channel}
mkdir -p %{buildroot}%{_mandir}/man1/

pushd %{target}
cp -a *.pak locales resources %{buildroot}%{chromium_path}
cp -a chrome %{buildroot}%{chromium_path}/%{chromium_browser_channel}
cp -a chrome_sandbox %{buildroot}%{chromium_path}/chrome-sandbox
cp -a chromedriver %{buildroot}%{chromium_path}/chromedriver
cp -a chrome.1 %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
cp -a libffmpegsumo.so %{buildroot}%{chromium_path}
cp -a libpdf.so %{buildroot}%{chromium_path}/libpdf.so
cp -a icudtl.dat %{buildroot}%{chromium_path}
popd

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp -a chrome/app/theme/chromium/product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{chromium_browser_channel}.png

mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE4}

%if %{flash}
# Bundle PepperFlash from Chrome's rpm
mkdir -p %{buildroot}%{chromium_path}/PepperFlash
%ifarch x86_64
	cp -a %{SOURCE8} %{buildroot}%{chromium_path}/PepperFlash/libpepflashplayer.so
	cp -a %{SOURCE9} %{buildroot}%{chromium_path}/PepperFlash/manifest.json
%else
	cp -a %{SOURCE11} %{buildroot}%{chromium_path}/PepperFlash/libpepflashplayer.so
	cp -a %{SOURCE12} %{buildroot}%{chromium_path}/PepperFlash/manifest.json
%endif
%endif

%check
%if %{tests}
	Xvfb :9 -screen 0 1024x768x24 &

	export XVFB_PID=$!
	export LC_ALL="en_US.utf8"
	export DISPLAY=:9

	# Disable failed tests
	pushd %{target}
	(
	./base_unittests \
		--gtest_filter=\
			-FileUtilTest.ChangeDirectoryPermissionsAndEnumerate \
			-FileUtilTest.ChangeFilePermissionsAndRead \
			-FileUtilTest.ChangeFilePermissionsAndWrite \
			-OutOfMemoryDeathTest.ViaSharedLibraries \
	&& \
	./cacheinvalidation_unittests && \
	./content_unittests \
		--gtest_filter=\
			-BaseFileTest.ReadonlyBaseFile \
			-BaseFileTest.RenameWithError \
			-DownloadFileTest.RenameError \
			-SharedCryptoTest.AesKwRawSymkeyUnwrapCorruptData \
	&& \
	./crypto_unittests && \
	./net_unittests
		--gtest_filter=\
			-UDPSocketTest.Broadcast \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/0 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/1 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/2 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/3 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/4 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/5 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/6 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/7 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/8 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/9 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/10 \
			-Spdy/SpdyNetworkTransactionTest.UnreadableFilePost/11 \
			-NextProto/HttpNetworkTransactionTest.UploadUnreadableFile/0 \
			-NextProto/HttpNetworkTransactionTest.UploadUnreadableFile/1 \
			-NextProto/HttpNetworkTransactionTest.UploadUnreadableFile/2 \
			-NextProto/HttpNetworkTransactionTest.UploadUnreadableFile/3 \
	&& \
	./printing_unittests && \
	./sql_unittests) || ( kill $XVFB_PID; unset XVFB_PID )
	popd

	kill $XVFB_PID
	unset XVFB_PID
%endif

%clean
rm -rf %{buildroot}

%post
# Set SELinux execmem_exec_t label
semanage fcontext -a -t execmem_exec_t /%{chromium_path}/%{chromium_browser_channel}
restorecon -R -v /%{chromium_path}/%{chromium_browser_channel}

touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
	touch --no-create %{_datadir}/icons/hicolor &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root,-)
%{_bindir}/%{chromium_browser_channel}
%dir /%{chromium_path}
/%{chromium_path}/*.pak
/%{chromium_path}/%{chromium_browser_channel}
/%{chromium_path}/%{chromium_browser_channel}.sh

%attr(4755, root, root) /%{chromium_path}/chrome-sandbox
%attr(755, root, root) /%{chromium_path}/chromedriver

/%{chromium_path}/libffmpegsumo.so
/%{chromium_path}/libpdf.so
/%{chromium_path}/icudtl.dat
/%{chromium_path}/locales/
/%{chromium_path}/resources/
%{_mandir}/man1/%{chromium_browser_channel}.*
%{_datadir}/icons/hicolor/256x256/apps/%{chromium_browser_channel}.png
%{_datadir}/applications/*.desktop

%if %{?flash}
/%{chromium_path}/PepperFlash

%attr(775, root, root) /%{chromium_path}/PepperFlash/libpepflashplayer.so
%endif

%changelog
* Mon Nov 10 2014 Matthias Grosser <mtgrosser@gmx.net> 38.0.2125.104-1.el6.centos
- enable chromedriver

* Fri Nov  7 2014 Johnny Hughes <johnny@centos.org> 38.0.2125.104-1.el6.centos
- change the api keys

* Thu Oct 16 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.104-1
- Update to 38.0.2125.104
- Resolves: rhbz#1153012

* Thu Oct 09 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-2
- The boringssl is used for tests, without the possibility of using
  the system openssl instead. Remove the openssl and boringssl sources
  when not building the tests.
- Resolves: rhbz#1004948

* Wed Oct 08 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-1
- Update to 38.0.2125.101
- System openssl is used for tests, otherwise the bundled boringssl is used
- Don't build with clang
- Resolves: rhbz#1004948

* Wed Sep 10 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.120-1
- Update to 37.0.2062.120
- Resolves: rhbz#1004948

* Wed Aug 27 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.94-1
- Update to 37.0.2062.94
- Include the pdf viewer library

* Wed Aug 13 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.143-1
- Update to 36.0.1985.143
- Use system openssl instead of bundled one
- Resolves: rhbz#1004948

* Thu Jul 17 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.125-1
- Update to 36.0.1985.125
- Add libexif as BR
- Resolves: rhbz#1004948

* Wed Jun 11 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.153-1
- Update to 35.0.1916.153
- Resolves: rhbz#1004948

* Wed May 21 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.114-1
- Update to 35.0.1916.114
- Bundle python-argparse
- Resolves: rhbz#1004948

* Wed May 14 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.137-1
- Update to 34.0.1847.137
- Resolves: rhbz#1004948

* Mon May 5 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.132-1
- Update to 34.0.1847.132
- Bundle depot_tools and switch from make to ninja
- Remove PepperFlash
- Resolves: rhbz#1004948

* Mon Feb 3 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.102-1
- Update to 32.0.1700.102

* Thu Jan 16 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.77-1
- Update to 32.0.1700.77
- Properly kill Xvfb when tests fails
- Add libdrm as BR
- Add libcap as BR

* Tue Jan 7 2014 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-2
- Minor changes in spec files and scripts
- Add Xvfb as BR for tests
- Add policycoreutils-python as Requires
- Compile unittests and run them in chech phase, but turn them off by default
  as many of them are failing in Brew

* Thu Dec 5 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-1
- Update to 31.0.1650.63

* Thu Nov 21 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.57-1
- Update to 31.0.1650.57

* Wed Nov 13 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.48-1
- Update to 31.0.1650.48
- Minimal supported RHEL6 version is now RHEL 6.5 due to GTK+

* Fri Oct 25 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.114-1
- Update to 30.0.1599.114
- Hide the infobar with warning that this version of OS is not supported
- Polished the chromium-latest.py

* Thu Oct 17 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.101-1
- Update to 30.0.1599.101
- Minor changes in scripts

* Wed Oct 2 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.66-1
- Update to 30.0.1599.66
- Automated the script for cleaning the proprietary sources from ffmpeg.

* Thu Sep 19 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.76-1
- Update to 29.0.1547.76
- Added script for removing the proprietary sources from ffmpeg. This script is called during cleaning phase of ./chromium-latest --rhel

* Mon Sep 16 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-2
- Compile with Dproprietary_codecs=0 and Dffmpeg_branding=Chromium to disable proprietary codecs (i.e. MP3)

* Mon Sep 9 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-1
- Initial version based on Tom Callaway's <spot@fedoraproject.org> work
