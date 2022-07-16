from random import choices
from lib.ec2_services import Ec2_service
# ubuntu="ami-012ae45a4a2d92750"
# amazon="ami-0917076ab9780844d"
class services_menu:
    def __init__(self):
        self.__ec2=Ec2_service()
    def start(self):
        print("Welcome to AWS")
        run = False
        while run != True:
            choice=int(input(
                 "1. Show security groups\n2. Create security group\n3. Delete security group\n4. Show instances\n5. Create instance\n6. Delete instance\n0. Exit\n"))
            if choice == 1:
                self.__ec2.show_security_groups()
            elif choice == 2:
                groupName = input("Enter name your group...\n")
                self.__ec2.add_security_groups(groupName)
            elif choice == 3:
                groupName = input("Enter name your group...\n")
                self.__ec2.delete_security_group(groupName)
            elif choice == 4:
                self.__ec2.show_all_instance()
            elif choice == 5:
                image=(input(
                    "Enter image ami(\n1.Ubuntu - ami-012ae45a4a2d92750 \n2.Amazon - ami-0917076ab9780844d)\n3.SUSE - ami-04989fe7f688013eb\n4.Debian 11 - ami-00189fd46154b0f9d\n 5.Red Hat Enterprise Linux 8 - ami-06a2a41d455060f8b\n "
                    ))
                instanceType=(input("Enter instance type (\nt3.micro\nt2.micro) "))
                keyName=(input("Enter keyName (Stockholm_RSA) "))
                choices=int(input("Do you create security group\n (1.Yes 2.No)"))
                if choices == 1:
                    self.__ec2.create_instance_with_created_security_group(image,instanceType,keyName)
                else:
                    sg_id=input("Enter security group id \n(Default - sg-05eefaef33dc0600c)\n")
                    self.__ec2.create_instance_with_attached_security_group(image,instanceType,keyName,sg_id)
                self.__ec2.instances[0].wait_until_running()
                print("Instance was created!!!!")
                self.__ec2.instances[0].reload()
                print(f"Public IP your instance {self.__ec2.instances[0].id} is {self.__ec2.instances[0].public_ip_address}")
            elif choice == 6:
                id=input("Enter id your instance... \n")
                self.__ec2.delete_instance(id)
            elif choice == 0:
                run = True  
            else:
                print("You enter invalid value!!!!")

    


