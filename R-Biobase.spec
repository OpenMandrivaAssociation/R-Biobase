%bcond_with internet
%bcond_with bootstrap
%global packname  Biobase
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.14.0
Release:          4
Summary:          Biobase: Base functions for Bioconductor
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Biobase.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/Biobase_2.14.0.tar.gz
Requires:         R-utils 
Requires:         R-methods
%if %{with bootstrap}
Requires:         R-tools
%else 
Requires:         R-tools R-tkWidgets R-ALL 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils
BuildRequires:    R-methods 
%if %{with bootstrap}
BuildRequires:    R-tools
%else
BuildRequires:    R-tools R-tkWidgets R-ALL 
%endif

%description
Functions that are needed by many other packages or which replace R

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
    %if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
    %endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Code
%{rlibdir}/%{packname}/ExpressionSet
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/UnitTests
%{rlibdir}/%{packname}/testClass.R


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.14.0-2
+ Revision: 778316
- Rebuild without bootstrap.

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.14.0-1
+ Revision: 775487
- Import R-Biobase
- Import R-Biobase

