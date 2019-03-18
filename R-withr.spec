#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-withr
Version  : 2.1.2
Release  : 49
URL      : https://cran.r-project.org/src/contrib/withr_2.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/withr_2.1.2.tar.gz
Summary  : Run Code 'With' Temporarily Modified Global State
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-DBI
BuildRequires : R-assertthat
BuildRequires : R-markdown
BuildRequires : R-mime
BuildRequires : buildreq-R

%description
# Withr - Run Code âWithâ Modified State
[![Travis-CI Build
Status](https://travis-ci.org/r-lib/withr.svg?branch=master)](https://travis-ci.org/r-lib/withr)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/r-lib/withr?branch=master&svg=true)](https://ci.appveyor.com/project/jimhester/withr)
[![Coverage
status](https://codecov.io/gh/r-lib/withr/branch/master/graph/badge.svg)](https://codecov.io/github/r-lib/withr?branch=master)
[![CRAN
Version](http://www.r-pkg.org/badges/version/withr)](http://www.r-pkg.org/pkg/withr)

%prep
%setup -q -c -n withr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552834358

%install
export SOURCE_DATE_EPOCH=1552834358
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library withr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library withr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library withr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  withr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/withr/DESCRIPTION
/usr/lib64/R/library/withr/INDEX
/usr/lib64/R/library/withr/Meta/Rd.rds
/usr/lib64/R/library/withr/Meta/features.rds
/usr/lib64/R/library/withr/Meta/hsearch.rds
/usr/lib64/R/library/withr/Meta/links.rds
/usr/lib64/R/library/withr/Meta/nsInfo.rds
/usr/lib64/R/library/withr/Meta/package.rds
/usr/lib64/R/library/withr/Meta/vignette.rds
/usr/lib64/R/library/withr/NAMESPACE
/usr/lib64/R/library/withr/NEWS.md
/usr/lib64/R/library/withr/R/withr
/usr/lib64/R/library/withr/R/withr.rdb
/usr/lib64/R/library/withr/R/withr.rdx
/usr/lib64/R/library/withr/doc/index.html
/usr/lib64/R/library/withr/doc/withr.R
/usr/lib64/R/library/withr/doc/withr.Rmd
/usr/lib64/R/library/withr/doc/withr.html
/usr/lib64/R/library/withr/help/AnIndex
/usr/lib64/R/library/withr/help/aliases.rds
/usr/lib64/R/library/withr/help/paths.rds
/usr/lib64/R/library/withr/help/withr.rdb
/usr/lib64/R/library/withr/help/withr.rdx
/usr/lib64/R/library/withr/html/00Index.html
/usr/lib64/R/library/withr/html/R.css
/usr/lib64/R/library/withr/tests/testthat.R
/usr/lib64/R/library/withr/tests/testthat/helper.R
/usr/lib64/R/library/withr/tests/testthat/test-connection.R
/usr/lib64/R/library/withr/tests/testthat/test-db.R
/usr/lib64/R/library/withr/tests/testthat/test-defer.R
/usr/lib64/R/library/withr/tests/testthat/test-devices.R
/usr/lib64/R/library/withr/tests/testthat/test-file.R
/usr/lib64/R/library/withr/tests/testthat/test-local.R
/usr/lib64/R/library/withr/tests/testthat/test-namespace.R
/usr/lib64/R/library/withr/tests/testthat/test-sink.R
/usr/lib64/R/library/withr/tests/testthat/test-tempfile.R
/usr/lib64/R/library/withr/tests/testthat/test-with.R
/usr/lib64/R/library/withr/tests/testthat/test-wrap.R
