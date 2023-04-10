datadir="Datasets"
mkdir $datadir
chmod a+rwx $datadir
command -v lynx > /dev/null || { echo "Error: lynx is required to run the script"; exit 1; }
lynx -dump http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/ | grep -oe 'http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/\(scp.*\.txt\)' | wget -P $datadir -i - -nv 

