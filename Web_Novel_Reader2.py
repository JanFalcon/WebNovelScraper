#
# read the data from the URL and print it
#
import urllib.request


def main():
    # open a connection to a URL using urllib2
    web_url = urllib.request.urlopen("https://www.youtube.com/user/guru99com")

    # get the result code and print it
    print("result code: " + str(web_url.getcode()))

    # read the data from the URL and print it
    data = web_url.read()
    print(data)


if __name__ == "__main__":
    main()
