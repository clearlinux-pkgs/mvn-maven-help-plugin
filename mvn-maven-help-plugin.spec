#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-help-plugin
Version  : 3.2.0
Release  : 4
URL      : https://github.com/apache/maven-help-plugin/archive/maven-help-plugin-3.2.0.tar.gz
Source0  : https://github.com/apache/maven-help-plugin/archive/maven-help-plugin-3.2.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-help-plugin/maven-metadata.xml
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-help-plugin-data = %{version}-%{release}

%description
<!---
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

%package data
Summary: data components for the mvn-maven-help-plugin package.
Group: Data

%description data
data components for the mvn-maven-help-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/maven-metadata-central.xml


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/3.2.0/maven-help-plugin-3.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-help-plugin/maven-metadata-central.xml
