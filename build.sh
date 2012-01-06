#!/bin/bash

### WARNING: DO NOT CHANGE CODES from HERE !!! ###
#import setup
cd `dirname $0`
_PWD=`pwd`
pushd ./ > /dev/null
while [ ! -f "./xo-setup.conf" ]
do
    cd ../
    SRCROOT=`pwd`
    if [ "$SRCROOT" == "/" ]; then
        echo "Cannot find xo-setup.conf !!"
        exit 1
    fi
done
popd > /dev/null
. ${SRCROOT}/xo-setup.conf
cd ${_PWD}
### WARNING: DO NOT CHANGE CODES until HERE!!! ###

export VERSION=1.0

CFLAGS="${CFLAGS}"

if [ $1 ];
then
     make $1 || exit 1
else
     ./autogen.sh || exit 1
     ./configure --prefix=$PREFIX || exit 1
     make || exit 1
     make install || exit 1
     make_pkg.sh || exit 1   
fi

