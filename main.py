import os

import pytest

if __name__ == '__main__':
    pytest.main(['-v', '--alluredir', './allure-result', './cases', '--clean-alluredir'])
    os.system('/opt/homebrew/bin/allure generate ./allure-result/ - o ./allure-report/ --clean')
