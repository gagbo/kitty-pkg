%define version_string 0.10.0

%global __python %{__python3}
%global git_rev  v%{version_string}
%global checkout %{git_date}git%(c=%{git_rev}; echo ${c:0:7})

Name:           kitty
Version:        %{version_string}
Release:        1%{?dist}
Summary:        A modern, hackable, featureful, OpenGL-based terminal emulator

License:        GPLv3
URL:            https://github.com/kovidgoyal/kitty
Source0:        https://github.com/kovidgoyal/%{name}/archive/%{git_rev}.tar.gz
BuildArch:      x86_64

BuildRequires: python3-devel >= 3.5.0 harfbuzz-devel >= 1.5.0 zlib pkg-config
BuildRequires: libpng-devel freetype-devel fontconfig-devel libXcursor-devel
BuildRequires: libXrandr-devel libXinerama-devel libxkbcommon-x11-devel
BuildRequires: mesa-libGL-devel libXi-devel
# Add (gcc | clang) in the BuildRequires

Requires: harfbuzz libpng freetype fontconfig

%description
kitty - A terminal emulator
* Uses OpenGL for rendering, offloads rendering to the GPU for lower system
  load and buttery smooth scrolling. Uses threaded rendering to minimize input latency.
* Supports all modern terminal features: graphics (images), unicode,
  true-color, OpenType ligatures, mouse protocol, focus tracking, bracketed
  paste and so on.
* Supports tiling multiple terminal windows side by side in different layouts
  without needing to use an extra program like tmux
* Can be controlled from scripts or the shell prompt, even over SSH.
* Has a framework for kittens, small terminal programs that can be used to
  extend kitty’s functionality. For example, they are used for Unicode
  input and URL hints.
* Supports startup sessions which allow you to specify the window/tab
  layout, working directories and programs to run on startup.
* Cross-platform support: kitty currently works on Linux and macOS, but
  because it uses only OpenGL for rendering, it should be trivial to port
  to other platforms.
* Allows you to open the scrollback buffer in a separate window using
  arbitrary programs of your choice. This is useful for browsing the
  history comfortably in a pager or editor.


%prep
%setup -q -n %{name}-%{version_string}


%build
python3 setup.py linux-package --debug --libdir-name %{_lib}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr
cp -r linux-package/* %{buildroot}/usr


%check


%files
%{_bindir}/kitty
%{_libdir}/kitty/*
%{_datadir}/applications/kitty.desktop
%{_datadir}/terminfo/x/xterm-kitty
%{_datadir}/icons/hicolor/256x256/apps/kitty.png

%license LICENSE

%changelog
* Tue May 22 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.10.0-1
- Upgrade to release 0.10.0

* Fri May 11 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.9.1-1
- Upgrade to release 0.9.1

* Tue Apr 17 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.9.0-1
- Upgrade to release 0.9.0

* Tue Apr 3 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.4-1
- Upgrade to release 0.8.4

* Thu Mar 29 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.3-3
- Include commit 94d248d that fixes startup issue (see issue #421 upstream)

* Thu Mar 29 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.3-2
- Upgrade to release 0.8.3

