__version__ = '1.0.14'

# import requests
#
# _plotly_pypi_url = "https://pypi.python.org/pypi/plotly"


# def check_version():
#     msg = ""
#     succeded = True
#     try:
#         response = requests.get(_plotly_pypi_url)
#         title = response.text.split('<title>')[1].split('</title>')[0]
#         newest_version = title.split(' ')[1]
#         msg += "Newest version: {}\n".format(newest_version)
#     except:
#         succeded = False
#         msg += "Check {} for the newest version.\n".format(_plotly_pypi_url)
#     msg += "Your version:   {}\n\n".format(__version__)
#     if succeded:
#         if newest_version != __version__:
#             msg += "Looks like you might be running an old version of our " \
#                    "Python API. Don't fret, just run:\n\n" \
#                    "pip install --upgrade plotly\n\n" \
#                    "to get our newest release.\n"
#     return msg
