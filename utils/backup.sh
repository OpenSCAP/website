#!/bin/bash

die() { echo "$@" 1>&2 ; exit 1; }

which rhc || die "rhc executable not found. run 'dnf install rubygem-rhc'"

# You need to have rights to access www-rhopenscap.rhcloud.com
rhc snapshot save -a www -n rhopenscap -f portal-snapshot.tar.gz
# DO NOT SHARE THE SNAPSHOT!

# To restore run the following:
# THINK THINK THINK before you do this! Doing this will OVERWRITE
# the application with the snapshot!
# rhc snapshot restore -a www -n rhopenscap -f portal-snapshot-iamsure.tar.gz
