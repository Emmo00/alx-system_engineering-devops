# install flask
class pypackage {

  package { 'flask':
    ensure   => 'installed',
    provider => 'pip3',
  }

}
