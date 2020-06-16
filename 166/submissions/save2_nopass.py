import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        
        list_env = self.config['tox']['envlist'].split()
        list_env = [x.strip(',') for x in list_env]
        
        return list_env

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        
        basepython = set()
        
        for key in self.config.sections():
            
            options = self.config.options(key)
            
            if 'basepython' in options:
                
                basepython.add(self.config[key]['basepython'])
                
        return list(basepython)