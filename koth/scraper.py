import lxml.html
import os
import requests


def scrape(question, folder='bots'):
    '''
    Scrapes bots from Stack Exchange question and writes them to files. The
    name of each file is the first header in an answer, and the content is
    the first code block, for answers following the following format:

        # Header

        ```
        code
        ```

    Variants on this will work, as long as there is at least one h1 header and
    one code block. Answers that cannot be parsed will be ignored.
    Parameters:
     - question: the question URL, required.
     - folder: the folder to place the scripts in. Default "bots".
    Returns:
    The file paths of each scraped bot.
    '''
    # Get the web page.
    res = requests.get(question)
    # Parse it as HTML.
    xml = lxml.html.fromstring(res.text)
    ret = []
    # For each answer:
    for post in xml.xpath('.//div[@class="answer"]'):
        try:
            # Get the first header and code block.
            script = post.xpath('.//code')[0].text
            name = post.xpath('.//h1')[0].text_content()
        except IndexError:
            continue
        # Save it to a file.
        file = os.path.join(folder, name)
        with open(file, 'w') as f:
            f.write(script)
        # Make file executable.
        os.chmod(file, 0o775)
        ret.append(file)
    return ret
