import tilepaper.config
from nose.tools import eq_, raises
import tempfile
import yaml


class testConfig(object):
    """
    Test configuration loading
    """

    def test_load(self):
        """
        Load a config file and ensure it's a dict
        """

        config = tilepaper.config.load('./example-config.yml')
        eq_(type(config), dict)
        eq_(type(config['sizes']), list)

    @raises(IOError)
    def test_missing(self):
        """
        Raises exception for file not found
        """

        tilepaper.config.load('./not-found.yml')

    def test_defaults(self):
        """
        Test config is updated to incude defaults
        """

        tempconfig = tempfile.mkstemp()[1]
        config = {
            "sizes": [
                "100x100"
            ],
            "border": {
                "size": 5,
            },
            "grid": {
                "": [5, 4]
            }
        }
        with open(tempconfig, 'w') as f:
            f.write(yaml.safe_dump(config))

        config = tilepaper.config.load(tempconfig)
        eq_(config['sizes'], ['100x100'])
        eq_(config['inclusions'], 5)
        eq_(config['border']['color'], '000')
