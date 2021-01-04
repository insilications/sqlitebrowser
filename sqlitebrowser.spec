#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : sqlitebrowser
Version  : 3.12.1
Release  : 2
URL      : file:///insilications/build/clearlinux/packages/sqlitebrowser/sqlitebrowser-v3.12.1.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/sqlitebrowser/sqlitebrowser-v3.12.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: sqlitebrowser-bin = %{version}-%{release}
Requires: sqlitebrowser-data = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : gcc-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Help)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickControls2)
BuildRequires : pkgconfig(Qt5QuickTest)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5X11Extras)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(sqlcipher)
BuildRequires : pkgconfig(zlib)
BuildRequires : qtbase
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsvg
BuildRequires : qtsvg-dev
BuildRequires : qttools-dev
BuildRequires : readline-dev
BuildRequires : sqlcipher-dev
BuildRequires : sqlcipher-staticdev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
TS files for the application should be all named according to a convention such as <short_appname>_<locale>, e.g. sqlb_de, sqlb_ru etc.

%package bin
Summary: bin components for the sqlitebrowser package.
Group: Binaries
Requires: sqlitebrowser-data = %{version}-%{release}

%description bin
bin components for the sqlitebrowser package.


%package data
Summary: data components for the sqlitebrowser package.
Group: Data

%description data
data components for the sqlitebrowser package.


%prep
%setup -q -n sqlitebrowser
cd %{_builddir}/sqlitebrowser

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609788260
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fno-plt -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
#
export CXXFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fno-plt -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
#
export FCFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fno-plt -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export FFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fno-plt -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export CFFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fno-plt -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
#
export LDFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fno-plt -ffat-lto-objects -fPIC -pthread -lpthread -static-libstdc++ -static-libgcc /usr/lib64/libsqlcipher.a /usr/lib64/libcrypto.a /usr/lib64/libssl.a /usr/lib64/libz.a /usr/lib64/liblzma.a -pthread -ldl -lm -lmvec"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
%global _lto_cflags %{nil}
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
%cmake .. -DCMAKE_BUILD_TYPE=Release \
-Dsqlcipher=1 \
-Wno-dev
make  %{?_smp_mflags}  V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats
popd

%install
export SOURCE_DATE_EPOCH=1609788260
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlitebrowser

%files data
%defattr(-,root,root,-)
/usr/share/applications/sqlitebrowser.desktop
/usr/share/icons/hicolor/256x256/apps/sqlitebrowser.png
/usr/share/icons/hicolor/scalable/apps/sqlitebrowser.svg
/usr/share/metainfo/sqlitebrowser.desktop.appdata.xml
