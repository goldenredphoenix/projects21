from schedule_1 import Schedule


# def normalize_string(s):
#     s = map(lambda x: x.title(), s.strip().split(" "))
#     s = " ".join(list(s))
#     return s


# def main():
#     msgs = [
#         "Enter the full name of the first doctor: ",
#         "Enter the speciality of the first doctor: ",
#         "Enter the full name of the second doctor: ",
#         "Enter the speciality of the second doctor: "
#     ]
#     vars = []
#     for msg in msgs:
#         var = input(msg)
#         vars.append(normalize_string(var))

#     shd1 = Schedule(name=vars[0], speciality=vars[1])
#     shd2 = Schedule(name=vars[2], speciality=vars[3])

#     print(shd1.description,
#           shd1.doctor_name,
#           shd1.doctor_speciality,
#           shd2.doctor_name,
#           shd2.doctor_speciality, 
#           sep="\n")

#     return shd1, shd2


# if __name__ == "__main__":
#     main()



def normalize_string(s):
    s = map(lambda x: x.title(), s.strip().split(" "))  #
    s = " ".join(list(s))
    return s



def main():
    full_name = input("Enter the full name of the first doctor: ")
    speciality =  input("Enter the speciality of the first doctor: ")
    full_name_2 = input("Enter the full name of the second doctor: ")
    speciality_2 = input("Enter the speciality of the second doctor: ")
    full_name = normalize_string(full_name)

    shd1 = Schedule(name=full_name, speciality=speciality)
    shd2 = Schedule(name=full_name_2, speciality=speciality_2)

    print(shd1.description,
          shd1.doctor_name,
          shd1.doctor_speciality,
          shd2.doctor_name,
          shd2.doctor_speciality, 
          sep="\n")

    return shd1, shd2


if __name__ == "__main__":
     main()