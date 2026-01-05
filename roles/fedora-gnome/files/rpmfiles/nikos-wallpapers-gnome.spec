Name: nikos-wallpapers-gnome
Version: 1.0
Release: 1
Summary: A custom package for a installing custom wallpapers
License: MIT
BuildArch: noarch

%description
This package installs the custom wallpapers directory at /usr/share/gnome-background-properties

%install
# Create the target directory inside the build root
mkdir -p %{buildroot}/usr/share/gnome-background-properties

# Copy the font files from the source directory to the build root
cp -a %{_sourcedir}/gnome-background-properties/* %{buildroot}/usr/share/gnome-background-properties

%files
/usr/share/gnome-background-properties
