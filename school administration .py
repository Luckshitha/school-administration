import csv
def write_into_csv(info_list):
    with open ('student_info.csv', 'a', newline='')as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_num", "Email-id"])
        writer.writerow(info_list)
condition=True
while(condition):
    student_info=input("enter student info in the following format(Name Age Contact_num Email-id) :")
    print("Entered student info:"+ student_info)

    student_info_list=student_info.split(' ')


    print("\nThe entered info : + \nName:"+  student_info_list[0] +"\nAge:"+student_info_list[1] +"\nContact_num:"+student_info_list[2] +"\nEmail-id:"+student_info_list[3])



    check_info=input("Is the entered info correct?(yes/no):")
    if check_info=="yes":
        write_into_csv, (student_info_list)
        condition_check=input("do you want to enter info for another student(yes/no):")
        if condition_check=="yes":
            condition =True
        elif condition_check=="no":
            condition=False

    elif check_info=="no":
        print("please enter the correct info")
