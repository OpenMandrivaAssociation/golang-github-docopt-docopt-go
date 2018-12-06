%global debug_package	%{nil}
%global provider	github
%global provider_tld	com
%global project		docopt
%global repo		docopt.go
%global gorepo		docopt-go
%global github_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path	%{provider}.%{provider_tld}/%{project}/%{gorepo}
%global commit		854c423c810880e30b9fecdabb12d54f4a92f9bb
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		golang-github-docopt-docopt-go
Version:	0
Release:	0.10.git.%{shortcommit}%{?dist}
Summary:	Command-line interface description language in Go

License:	MIT
URL:		https://godoc.org/%{github_path}
Source0:	https://%{github_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

ExclusiveArch:	%{go_arches}

%description
Docopt helps you create beautiful command-line interfaces easily with Go


%package devel
BuildRequires:	golang >= 1.2.1-3
Requires:	golang >= 1.2.1-3
Summary:	Command-line interface description language in Go
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
Docopt helps you create beautiful command-line interfaces easily with Go

This package contains library source intended for building other packages
which use docopt/docopt-go.


%prep
%setup -q -n %{repo}-%{commit}


%build


%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav docopt.go docopt_test.go testcases.docopt test_golang.docopt \
  %{buildroot}/%{gopath}/src/%{import_path}/


%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}


%files devel
%doc LICENSE README.md example_test.go examples
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep  7 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0-0.8.git.854c423
- Build for supported go_arches only

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git.854c423
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git.854c423
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git.854c423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0-0.1.git854c423c
- Initial package
