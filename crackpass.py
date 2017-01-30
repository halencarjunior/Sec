__author__ = 'bj'

import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dict.txt','r')

    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word,salt)


        if (str(cryptWord) == str(cryptPass)):
            print "[+] Senha Encontrada: " + word + "\n"
            return
    print "[-] Senha nao encontrada.\n"
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip('\n')
            print "[*] Cracking senha para usuario: " + user + " Com Senha: " + cryptPass
            testPass(cryptPass)

if __name__ == "__main__":
    main()