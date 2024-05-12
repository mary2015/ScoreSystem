import os

import pytest

if __name__ == '__main__':
    pytest.main(['-v', '--alluredir', './allure-results', './cases', '--clean-alluredir'])
    os.system('/opt/homebrew/bin/allure generate ./allure-results/ -o ./target/allure-report/ --clean')
