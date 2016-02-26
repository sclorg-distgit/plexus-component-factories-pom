%global pkg_name plexus-component-factories-pom
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global artifactId plexus-component-factories

Name:		%{?scl_prefix}%{pkg_name}
Version:	1.0
Release:	0.7.alpha11.13%{?dist}
Summary:	Plexus Component Factories POM
BuildArch:	noarch
License:	ASL 2.0
URL:		http://plexus.codehaus.org/
Source0:	http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/%{version}-alpha-11/%{artifactId}-%{version}-alpha-11.pom
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:	%{?scl_prefix}maven-local


%description
This package provides Plexus Component Factories parent POM used by different
Plexus packages.

%prep
%setup -cT -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_xpath_remove pom:modules
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_alias : plexus:
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1.0-0.7.alpha11.13
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0-0.7.alpha11.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0-0.7.alpha11.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.0-0.7.alpha11.10
- Fix directory ownership

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.9
- Rebuild to fix provides

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.7.alpha11.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.7.alpha11.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.7.alpha11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.7.alpha11
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.5.alpha11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.4.alpha11
- Build with xmvn

* Thu Dec 13 2012 Michal Srb <msrb@redhat.com> - 1.0-0.3.alpha11
- Fixed artifactId

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 1.0-0.2.alpha11
- Use direct link in Source0
- Improved prep/setup section
- mvn-rpmbuild verify is now in check section
- More specific files section
- add_maven_depmap macro now with -a option

* Mon Dec 10 2012 Michal Srb <msrb@redhat.com> - 1.0-0.1.alpha11
- Initial packaging

