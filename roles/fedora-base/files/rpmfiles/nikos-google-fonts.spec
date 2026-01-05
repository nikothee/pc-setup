Name: nikos-google-fonts
Version: 1.0
Release: 1
Summary: A custom package for a installing google fonts
License: MIT
BuildArch: noarch

%description
This package installs the google-fonts directory at /usr/share/fonts

%install
# Create the target directory inside the build root
mkdir -p %{buildroot}/usr/share/fonts/google-fonts/

# Copy the font files from the source directory to the build root
cp -a %{_sourcedir}/google-fonts/* %{buildroot}/usr/share/fonts/google-fonts/

%files
/usr/share/fonts/google-fonts/

# Ensure the font cache is updated on installation
%post
fc-cache -fv

%postun
fc-cache -fv
