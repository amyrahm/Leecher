#The Programs helps to extract subdomain & wordlist from from google dorking from full url




import sys
from urlparse import urlparse
import re
unique_domain=set()
unique_path=set()
while True:
    print "choose Options to extract things of your choice\n"
    print "1.Extract unique domains[1]"
    print "2.Extract keywords[2]"
    print "0.Exit"
    ch=raw_input("Enter choice :")
    if(ch=='1'):
        with open(sys.argv[1]) as fh:
            for line in fh:
                line= line.strip()
                domain= urlparse(line).netloc
                if domain.startswith('www.'):
                    domain= re.sub(r'www.', '', domain)
                    unique_domain.add(domain)
                else:
                    #print domain
                    unique_domain.add(domain)


        for elment in unique_domain:
            print elment
    elif(ch=='2'):
        with open(sys.argv[1]) as fh:
            for line in fh:
                line= line.strip()
                domainpath= urlparse(line).path
                #print domainpath
                domainpath=domainpath.split('/')

                for element in domainpath:
                    unique_path.add(element)
            for item in unique_path:
                print item

    else:
        break
