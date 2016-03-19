#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-withr
Version  : 1.0.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/withr_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/withr_1.0.1.tar.gz
Summary  : Run Code 'With' Temporarily Modified Global State
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-testthat
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
Withr - Run Code 'With' Modified State
======================================
[![Travis-CI Build Status](https://travis-ci.org/jimhester/withr.svg?branch=master)](https://travis-ci.org/jimhester/withr) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/jimhester/withr?branch=master&svg=true)](https://ci.appveyor.com/project/jimhester/withr) [![Coverage Status](https://img.shields.io/codecov/c/github/jimhester/withr/master.svg)](https://codecov.io/github/jimhester/withr?branch=master) [![CRAN Version](http://www.r-pkg.org/badges/version/withr)](http://www.r-pkg.org/pkg/withr)

%prep
%setup -q -c -n withr

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library withr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library withr


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/withr/DESCRIPTION
/usr/lib64/R/library/withr/INDEX
/usr/lib64/R/library/withr/Meta/Rd.rds
/usr/lib64/R/library/withr/Meta/hsearch.rds
/usr/lib64/R/library/withr/Meta/links.rds
/usr/lib64/R/library/withr/Meta/nsInfo.rds
/usr/lib64/R/library/withr/Meta/package.rds
/usr/lib64/R/library/withr/NAMESPACE
/usr/lib64/R/library/withr/NEWS.md
/usr/lib64/R/library/withr/R/withr
/usr/lib64/R/library/withr/R/withr.rdb
/usr/lib64/R/library/withr/R/withr.rdx
/usr/lib64/R/library/withr/help/AnIndex
/usr/lib64/R/library/withr/help/aliases.rds
/usr/lib64/R/library/withr/help/paths.rds
/usr/lib64/R/library/withr/help/withr.rdb
/usr/lib64/R/library/withr/help/withr.rdx
/usr/lib64/R/library/withr/html/00Index.html
/usr/lib64/R/library/withr/html/R.css
