import urllib

url = "http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip"
print "Downloading with urllib.."
filename, header = urllib.urlretrieve(url, "code.zip")
print filename, header
