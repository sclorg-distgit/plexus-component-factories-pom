%{?scl:%scl_package plexus-component-factories-pom}
%{!?scl:%global pkg_name %{name}}

%global artifactId plexus-component-factories

Name:		%{?scl_prefix}plexus-component-factories-pom
Version:	1.0
Release:	0.13.alpha11.1%{?dist}
Summary:	Plexus Component Factories POM
BuildArch:	noarch
Group:		Development/Libraries
License:	ASL 2.0
URL:		https://github.com/codehaus-plexus/plexus-component-factories
Source0:	http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/%{version}-alpha-11/%{artifactId}-%{version}-alpha-11.pom
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus:pom:)

%description
This package provides Plexus Component Factories parent POM used by different
Plexus packages.

%prep
%setup -n %{pkg_name}-%{version} -cT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_xpath_remove pom:modules

%build
%mvn_alias : plexus:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.0-0.13.alpha11.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.12.alpha11
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.9.alpha11
- Update upstream URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.alpha11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
