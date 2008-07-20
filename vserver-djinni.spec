Summary:	vserver-djinni - performing privileged tasks in unprivileged vservers
Summary(pl.UTF-8):	vserver-djinni - wykonywanie uprzywilejowanych zadań w nieuprzywilejowanych vserverach
Name:		vserver-djinni
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://enrico-scholz.de/fedora.us-build/files/%{name}-%{version}.tar.bz2
# Source0-md5:	54ec7b6666deb1a288817c1025a4c6d2
URL:		http://enrico-scholz.de/fedora.us-build/html/ar01s02.html#sec:components:vserver-djinni
BuildRequires:	util-vserver-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vserver-djinni is used to do privileged tasks like directory mounting
in unprivileged vservers.

To do this, a djinnid daemon is running in the privileged host-ctx and
listens on commands from the vservers. One of djinni's designgoals was
to enable a vserver-in-vserver functionality which is not doable with
current vserver patch.

%description -l pl.UTF-8
vserver-djinni służy do wykonywania uprzywilejowanych zadań w
nieuprzywilejowanych vserverach.

W tym celu w kontekście uprzywilejowanego hosta działa demon djinnid i
nasłuchuje poleceń od vserverów. Jednym z celów projektu jest
umożliwienie tworzenia vserverów w vserverach, co nie jest wykonywalne
z aktualną łatą vserver.

%prep
%setup -q

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
