Name:           ros-hydro-romeo-sensors
Version:        0.0.12
Release:        0%{?dist}
Summary:        ROS romeo_sensors package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-naoqi-sensors
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-naoqi-sensors
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy

%description
The romeo_sensors package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Nov 26 2014 Ha Dang <hris2003@gmail.com> - 0.0.12-0
- Autogenerated by Bloom

* Wed Nov 26 2014 Ha Dang <hris2003@gmail.com> - 0.0.11-0
- Autogenerated by Bloom

