
FROM fedora:28
RUN yum groupinstall "C Development Tools and Libraries" -y
RUN yum install git-core libdb-cxx-devel libdb-cxx openssl-devel libevent-devel  cppzmq-devel qrencode-devel protobuf-devel boost* boost-devel miniupnpc-devel.x86_64 qt-devel qt4-devel python2-devel python2 python2-pip -y
RUN pip install construct==2.5.2 scrypt
