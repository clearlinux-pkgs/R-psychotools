#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-psychotools
Version  : 0.7.0
Release  : 33
URL      : https://cran.r-project.org/src/contrib/psychotools_0.7-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/psychotools_0.7-0.tar.gz
Summary  : Psychometric Modeling Infrastructure
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-psychotools-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
item response data and paired comparisons), basic model fitting functions (for
  Bradley-Terry, Rasch, parametric logistic IRT, generalized partial credit,
  rating scale, multinomial processing tree models), extractor functions for
  different types of parameters (item, person, threshold, discrimination,
  guessing, upper asymptotes), unified inference and visualizations, and various
  datasets for illustration.  Intended as a common lightweight and efficient
  toolbox for psychometric modeling and a common building block for fitting
  psychometric mixture models in package "psychomix" and trees based on
  psychometric models in package "psychotree".

%package lib
Summary: lib components for the R-psychotools package.
Group: Libraries

%description lib
lib components for the R-psychotools package.


%prep
%setup -q -c -n psychotools
cd %{_builddir}/psychotools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632841658

%install
export SOURCE_DATE_EPOCH=1632841658
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psychotools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psychotools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psychotools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc psychotools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/psychotools/CITATION
/usr/lib64/R/library/psychotools/DESCRIPTION
/usr/lib64/R/library/psychotools/INDEX
/usr/lib64/R/library/psychotools/Meta/Rd.rds
/usr/lib64/R/library/psychotools/Meta/data.rds
/usr/lib64/R/library/psychotools/Meta/demo.rds
/usr/lib64/R/library/psychotools/Meta/features.rds
/usr/lib64/R/library/psychotools/Meta/hsearch.rds
/usr/lib64/R/library/psychotools/Meta/links.rds
/usr/lib64/R/library/psychotools/Meta/nsInfo.rds
/usr/lib64/R/library/psychotools/Meta/package.rds
/usr/lib64/R/library/psychotools/Meta/vignette.rds
/usr/lib64/R/library/psychotools/NAMESPACE
/usr/lib64/R/library/psychotools/NEWS
/usr/lib64/R/library/psychotools/R/psychotools
/usr/lib64/R/library/psychotools/R/psychotools.rdb
/usr/lib64/R/library/psychotools/R/psychotools.rdx
/usr/lib64/R/library/psychotools/data/ConspiracistBeliefs2016.rda
/usr/lib64/R/library/psychotools/data/FirstNames.rda
/usr/lib64/R/library/psychotools/data/GermanParties2009.rda
/usr/lib64/R/library/psychotools/data/MathExam14W.rda
/usr/lib64/R/library/psychotools/data/MemoryDeficits.rda
/usr/lib64/R/library/psychotools/data/PairClustering.rda
/usr/lib64/R/library/psychotools/data/Sim3PL.rda
/usr/lib64/R/library/psychotools/data/SoundQuality.rda
/usr/lib64/R/library/psychotools/data/SourceMonitoring.rda
/usr/lib64/R/library/psychotools/data/StereotypeThreat.rda
/usr/lib64/R/library/psychotools/data/VerbalAggression.rda
/usr/lib64/R/library/psychotools/data/YouthGratitude.rda
/usr/lib64/R/library/psychotools/demo/MathExam14W.R
/usr/lib64/R/library/psychotools/demo/VerbalAggression.R
/usr/lib64/R/library/psychotools/demo/toolbox1.R
/usr/lib64/R/library/psychotools/demo/toolbox2.R
/usr/lib64/R/library/psychotools/doc/index.html
/usr/lib64/R/library/psychotools/doc/toolbox-simulation.Rnw
/usr/lib64/R/library/psychotools/doc/toolbox-simulation.pdf
/usr/lib64/R/library/psychotools/help/AnIndex
/usr/lib64/R/library/psychotools/help/aliases.rds
/usr/lib64/R/library/psychotools/help/paths.rds
/usr/lib64/R/library/psychotools/help/psychotools.rdb
/usr/lib64/R/library/psychotools/help/psychotools.rdx
/usr/lib64/R/library/psychotools/html/00Index.html
/usr/lib64/R/library/psychotools/html/R.css
/usr/lib64/R/library/psychotools/tests/Examples/psychotools-Ex.Rout.save
/usr/lib64/R/library/psychotools/tests/elementary_symmetric_functions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/psychotools/libs/psychotools.so
/usr/lib64/R/library/psychotools/libs/psychotools.so.avx2
/usr/lib64/R/library/psychotools/libs/psychotools.so.avx512
