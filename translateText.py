# import stuff
import  subprocess
subprocess.check_call(['pip','install','googletrans-py'])

from googletrans import Translator

newtTranslator = Translator()

def transToMarathi (nameString):
      marValues = []
      values = nameString.split(" ")
      for val in values:
            EN_to_MR = newtTranslator.translate(val,'mr','en').text
            #print(EN_to_MR.text)
            marValues.append(EN_to_MR)
      marString = " ".join(str(marVal) for marVal in marValues)
      return marString


if __name__ == '__main__':
      fullName = input("Enter Text to be translated in Marathi")
      transToMarathi(print(fullName))