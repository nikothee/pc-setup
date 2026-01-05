Name: nikos-nerd-fonts
Version: 1.0
Release: 1
Summary: A custom package for a installing nerd fonts
License: MIT
BuildArch: noarch

%description
This package installs the nerd-fonts directory at /usr/share/fonts

%install
# Create the target directory inside the build root
mkdir -p %{buildroot}/usr/share/fonts/nerd-fonts/

# Copy the font files from the source directory to the build root
cp -a %{_sourcedir}/nerd-fonts/* %{buildroot}/usr/share/fonts/nerd-fonts/

%files
/usr/share/fonts/nerd-fonts/

# Ensure the font cache is updated on installation
%post
fc-cache -fv

%postun
fc-cache -fv
