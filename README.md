chromedriver_el7
================

In this repo we collect some infos on building current versions of chromium and chromedriver on CentOS 7.

## About

There's several reasons as to why not use the official google-chrome yum repo provided by google.

The chrome packages from this repo do some nasty things to your system, like force-enabling
the google repository in your yum.repos.d, and adding a cron job which re-installs the google repo in case
you disabled it manually. Of course, this cron job grabs root privileges. Furthermore, google-chrome depends on ```at``` and installs and force-enables the ```atd``` service in systemd.

All of this is not acceptable, especially when running on a server environment where the stability of a defined environment is the main requirement. So we decided to use ```rpmbuild``` to build the chromium and chromedriver binaries from scratch.

The source rpm provided is based on http://people.centos.org/hughesjr/chromium/6/SRPMS/

All we did was adding chromedriver to the spec.

## Current Versions

| Program       | Version       |
|---------------|---------------|
| ChromeDriver  | 2.10          |
| Chromium      | 38.0.2125.104 |

## Instructions

**Do NOT do this as root! You might damage your system!**

RPM building will take place in ```~/rpmbuild```.

#### Get the SRPM for chromium 
```wget http://downloads.onrooby.com/chromium/srpms/chromium-browser-38.0.2125.104-1.el7.centos.src.rpm```

#### Check integrity
```$ sha256sum chromium-browser-38.0.2125.104-1.el7.centos.src.rpm
57fe233ac86080829e48b3825511c86342ad679ef5f3e49c398631ece43a4998 chromium-browser-38.0.2125.104-1.el7.centos.src.rpm```

#### Install (as normal user)
```rpm -ivh chromium-browser-38.0.2125.104-1.el7.centos.src.rpm```

#### Build
```
cd ~/rpmbuild/SPECS
rpmbuild -ba chromium-browser.spec
```

When rpmbuild complains about missing dependencies (mostly devel packages), install them using
```# yum install <packagenames>``` or alternatively use ```# yum-builddep chromium-browser.spec```

On a CentOS minimal system with ```@'development tools'``` installed, we needed to

```# yum install gtk2-devel atk-devel nss-devel pciutils-devel gnome-keyring-devel cups-devel libudev-devel pulseaudio-libs-devel libXdamage-devel libXScrnSaver-devel libXtst-devel fontconfig-devel GConf2-devel dbus-devel glib2-devel gperf alsa-lib-devel libusb-devel libdrm-devel libcap-devel libexif-devel libgnome-keyring-devel```

## Binaries

We provide pre-built packages. Use at your own risk!

http://downloads.onrooby.com/chromium/rpms/

Packages are signed with our GPG key: http://downloads.onrooby.com/RPM-GPG-KEY-onrooby

## TODO

- Split packages into chromium and chromium-chromedriver
