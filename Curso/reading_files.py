#open("employes.txt", "w") #write
#open("employes.txt", "a") #add
#open("employes.txt", "r+") #read and write

# employe_file = open("employes.txt", "r") #read

# for employee in employe_file.readlines():
# print(employe_file.read())
# print(employe_file.readline())
# print(employe_file.readline())
# print(employe_file.readlines())
# print(employe_file.readlines()[2])
    # print(employee)

# employe_file.close()

# employe_file = open("employes.txt", "a")

# employe_file.write("\nMisds - mumur") #adiciona conteudo a file

# employe_file.close()


employe_file = open("employes.txt", "w") #sobrescreve a file e pode criar uma nova

employe_file.write("\nMisds - mumur") 

employe_file.close()