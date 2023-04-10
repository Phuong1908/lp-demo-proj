datadir="Datasets"
mkdir $datadir
mkdir $datadir/processed
mkdir $datadir/raw
chmod a+rwx $datadir
command -v lynx > /dev/null || { echo "Error: lynx is required to run the script"; exit 1; }
lynx -dump http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/ | grep -oe 'http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/\(scp.*\.txt\)' | wget -P $datadir/raw -i - -nv 

